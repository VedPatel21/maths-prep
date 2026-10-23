from build_math2255 import *
import itertools
checks=[]
def check(claim,truth):
 assert truth,claim;checks.append(claim)
def mm(a,b):
 # A separately written exact product, used to audit manually authored claims.
 return [[sum(F(str(a[i][k]))*F(str(b[k][j])) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def zero_relation(cols,co):return mm(cols,[[x] for x in co])==[[0] for _ in cols]
check('1.7.11 h=6 relation',zero_relation([[1,3,-1],[-1,-5,5],[4,7,6]],[-5,2,1]))
check('1.7.14 h=26 relation',zero_relation([[1,-5,1],[-1,7,1],[3,8,26]],[-6,-1,1]))
for h in [-100,F(1,3),0,16,100]:
 check('1.7.12 parameter relation '+str(h),zero_relation([[2,-6,8],[-4,7,h],[1,-3,4]],[3*h+28,h+16,5]))
 check('1.7.13 parameter relation '+str(h),zero_relation([[1,-2,3],[5,-9,h],[-3,6,-9]],[27-2*h,15-h,1]))
check('1.3.17 target relation',mm([[1,-2],[4,-3],[-2,7]],[[-2],[-3]])==[[4],[1],[-17]])
check('1.3.18 target relation',mm([[1,-3],[0,1],[-2,8]],[[F(-37,2)],[-5]])==[[F(-7,2)],[-5],[-3]])
check('1.3.35 mine output',mm([[20,30],[550,500]],[[F(3,2)],[4]])==[[150],[2825]])
# Independently audit the exact square inverse answers supplied in the sources.
for name,a,b in [
 ('1.1.11',[[0,1,4],[1,3,3],[3,7,5]],[[19],[-8],[1]]),
 ('1.4.11',[[1,2,4],[0,1,5],[-2,-4,-3]],[[0],[-3],[1]]),
 ('1.4.13',[[3,-5],[-2,6],[1,1]],[[F(5,2)],[F(3,2)]]),
 ('1.9.22',[[1,-2],[-1,3],[3,-2]],[[5],[3]])]:
 expected={'1.1.11':[[-4],[-2],[6]],'1.4.11':[[-2],[2],[9]],'1.4.13':[[0],[4],[4]],'1.9.22':[[-1],[4],[9]]}[name]
 check(name+' source selected result',mm(a,b)==expected)
for n in range(1,11):
 L=[[int(i>=j) for j in range(n)] for i in range(n)]
 Bi=[[int(i==j)-int(i==j+1) for j in range(n)] for i in range(n)]
 check('2.2.43 generalized inverse size '+str(n),mm(L,Bi)==ident(n) and mm(Bi,L)==ident(n))
 A=[[F(j+1)*int(i>=j) for j in range(n)] for i in range(n)]
 B=[[F(int(i==j)-int(i==j+1),i+1) for j in range(n)] for i in range(n)]
 check('2.2.44 generalized inverse size '+str(n),mm(A,B)==ident(n) and mm(B,A)==ident(n))
# Inventory has no repeated or missing complete visible numbered entries.
with (SRC/'exercise-inventory.csv').open() as f:rows=list(csv.DictReader(f))
check('339 unique source question IDs',len(rows)==339 and len({(r['section'],r['exercise']) for r in rows})==339)
check('337 solved, two explicitly truncated',sum(r['status']=='solved' for r in rows)==337 and sum(r['status']=='truncated source' for r in rows)==2)
# Assertions in authoring routines checked all generated steps and all generated parametric answers.
checks+=json.loads((SRC/'textbook-computation-checks.json').read_text())
checks+=json.loads((SRC/'workbook-computation-checks.json').read_text())
(SRC/'mathematical-qa.json').write_text(json.dumps({'passed_assertions':len(checks),'checks':checks},indent=2))
print(len(checks),'mathematical and inventory assertions passed')
