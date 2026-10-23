"""Question-only scan boundaries, shared instructions and verified transcriptions.
Coordinates refer to the immutable 1160 × 1500 source scans; no OCR is used.
"""
import json,re,ast
from pathlib import Path
Q={}
def add(sec,n,p,box):Q[f'{sec}.{n}']={'page':p,'box':box,'instruction':'','dependencies':[]}
def col(sec,p,x,r,items):
 for n,t,b in items:add(sec,n,p,[x,t,r,b])
def pairs(sec,p,x,mid,r,items):
 for n,t,b in items:
  add(sec,n,p,[x,t,mid-7,b]);add(sec,n+1,p,[mid,t,r,b])
def group(sec,nums,text):
 for n in nums:Q[f'{sec}.{n}']['instruction']=text
# Section 1.1
pairs('1.1',1,98,343,564,[(1,212,265),(7,452,545)])
# 7 and 8 are on the right, not the left.
Q['1.1.7']['box']=[585,452,818,545];Q['1.1.8']['box']=[818,452,1045,545]
col('1.1',1,98,565,[(3,287,495),(4,514,567)])
col('1.1',1,585,1045,[(5,128,225),(6,247,345),(9,566,667)])
col('1.1',2,105,580,[(10,127,230),(11,270,360),(12,375,461),(13,477,567),(14,582,672),(15,689,756),(16,765,833),(17,840,907),(18,915,984),(19,1045,1168),(20,1188,1315),(21,1320,1390)])
col('1.1',2,600,1080,[(22,135,203),(27,626,656),(28,664,713),(29,720,753),(30,758,810),(31,812,909),(32,916,950),(33,951,1000),(34,1005,1057),(35,1067,1200),(36,1205,1260),(37,1267,1400)])
pairs('1.1',2,600,835,1080,[(23,275,326),(25,335,386)])
group('1.1',range(1,3),'Solve each system by using elementary row operations on the equations or on the augmented matrix. Follow the systematic elimination procedure described in this section.')
group('1.1',[5,6],'Consider this matrix as the augmented matrix of a linear system. State in words the next two elementary row operations that should be performed in the process of solving the system.')
group('1.1',range(7,11),'The augmented matrix of a linear system has been reduced by row operations to the form shown. Continue the appropriate row operations and describe the solution set of the original system.')
group('1.1',range(11,15),'Solve the system.')
group('1.1',[19,20],'Determine if the system is consistent. Do not completely solve the system.')
group('1.1',range(23,27),'Determine the value(s) of h such that the matrix is the augmented matrix of a consistent linear system.')
# Section 1.2
col('1.2',3,88,570,[(1,180,367),(2,411,593)])
pairs('1.2',3,600,836,1090,[(3,125,200),(7,378,431),(9,441,497),(11,505,587)])
col('1.2',3,600,1090,[(5,208,281),(6,290,324),(13,598,695)])
col('1.2',4,75,565,[(14,134,239),(15,318,416),(16,423,519),(17,526,622),(18,628,724),(19,842,998),(20,1000,1155)])
pairs('1.2',4,75,312,565,[(21,1209,1268),(23,1350,1422)])
col('1.2',4,585,1080,[(25,200,271),(26,281,312),(27,318,371),(28,377,429),(29,438,488),(30,496,546),(31,555,607),(32,614,666),(33,671,746),(34,752,800),(35,807,861),(36,869,945),(37,951,1026),(38,1032,1108),(39,1114,1188),(40,1194,1269),(41,1273,1324)])
group('1.2',[1,2],'Determine which matrices are in reduced echelon form and which others are only in echelon form.')
group('1.2',[3,4],'Row reduce the matrix to reduced echelon form. Circle the pivot positions in the final matrix and in the original matrix, and list the pivot columns.')
group('1.2',range(7,15),'Find the general solution of the system whose augmented matrix is given.')
group('1.2',[19,20],'A filled square denotes a required nonzero leading entry; * is arbitrary (possibly zero). Suppose each matrix represents the augmented matrix for a system. Determine whether it is consistent, and if so, whether its solution is unique.')
group('1.2',[21,22],'Determine the value(s) of h such that the matrix is the augmented matrix of a consistent linear system.')
group('1.2',[23,24],'Choose h and k such that the system has (a) no solution, (b) a unique solution, and (c) many solutions. Give separate answers for each part.')
# Section 1.3
col('1.3',5,86,570,[(1,160,217),(2,224,282),(3,380,412),(4,380,412),(5,471,553),(6,556,612),(7,943,979),(8,981,1018)])
Q['1.3.3']['box']=[90,379,330,412];Q['1.3.4']['box']=[331,379,569,412]
pairs('1.3',5,592,830,1080,[(9,184,276)])
col('1.3',5,592,1080,[(11,347,427),(12,444,525),(13,584,664),(14,681,763),(15,844,924),(16,940,1021)])
col('1.3',6,88,574,[(17,123,230),(18,234,338),(19,342,450),(20,455,502),(21,507,581),(22,586,663),(23,727,786),(24,788,820),(25,823,926),(26,928,977),(27,984,1040),(28,1047,1095),(29,1101,1179),(30,1184,1235),(31,1240,1294),(32,1297,1378)])
col('1.3',6,589,1080,[(33,125,345),(34,352,530),(35,537,936),(36,944,1372)])
group('1.3',[1,2],'Compute u + v and u − 2v.')
group('1.3',[3,4],'Display the following vectors using arrows on an xy-graph: u, v, −v, −2v, u + v, u − v, and u − 2v. Notice that u − v is the vertex of a parallelogram whose other vertices are u, 0, and −v.')
group('1.3',[5,6],'Write a system of equations equivalent to the given vector equation.')
group('1.3',[7,8],'Use the accompanying figure to write each listed vector as a linear combination of u and v. Is every vector in ℝ² a linear combination of u and v?')
for n in [7,8]:Q[f'1.3.{n}']['extra']=[[5,130,688,531,937]]
group('1.3',[9,10],'Write a vector equation equivalent to the given system of equations.')
group('1.3',[11,12],'Determine if b is a linear combination of a₁, a₂, and a₃.')
group('1.3',[13,14],'Determine if b is a linear combination of the vectors formed from the columns of A.')
group('1.3',[15,16],'List five vectors in Span{v₁,v₂}. For each vector, show the weights on v₁ and v₂ used to generate the vector and list the three entries of the vector. Do not make a sketch.')
# Section 1.4
pairs('1.4',7,87,331,578,[(1,206,285),(3,297,377)])
col('1.4',7,590,1085,[(5,171,301),(6,302,401)])
col('1.4',8,100,575,[(7,128,234),(8,240,300),(11,548,631),(12,636,719),(13,736,1024),(14,1029,1140),(15,1143,1247),(16,1250,1331)])
pairs('1.4',8,100,344,575,[(9,359,454)])
col('1.4',8,595,1084,[(17,232,282),(18,291,340),(19,349,423),(20,430,503),(21,508,636),(22,641,746),(23,805,862),(24,866,919),(25,923,978),(26,982,1058),(27,1061,1117),(28,1121,1187),(29,1189,1220),(30,1223,1271),(31,1275,1332),(32,1335,1399)])
group('1.4',range(1,5),'Compute the product using (a) the definition, and (b) the row–vector rule for computing Ax. If a product is undefined, explain why.')
group('1.4',range(5,9),'Use the definition of Ax to write the matrix equation as a vector equation, or vice versa.')
group('1.4',[9,10],'Write the system first as a vector equation and then as a matrix equation.')
group('1.4',[11,12],'Given A and b, write the augmented matrix for the linear system corresponding to Ax = b. Then solve the system and write the solution as a vector.')
group('1.4',range(17,21),'These questions refer to the matrices A and B shown below. Make appropriate calculations that justify your answers and mention an appropriate theorem.')
for n in range(17,21):Q[f'1.4.{n}']['extra']=[[8,593,127,1080,232]]
# Section 1.5
pairs('1.5',9,128,356,578,[(1,275,367),(3,383,439),(5,535,627),(7,692,754),(9,756,815)])
col('1.5',9,124,580,[(11,815,916),(12,921,1023)])
col('1.5',9,598,1063,[(13,211,262),(14,270,322),(15,328,381),(16,387,440),(17,446,519),(18,527,621),(19,630,820),(20,826,987),(21,993,1047),(22,1050,1106)])
group('1.5',range(1,5),'Determine if the system has a nontrivial solution. Try to use as few row operations as possible.')
group('1.5',[5,6],'Follow the method of Examples 1 and 2 to write the solution set of the given homogeneous system in parametric vector form.')
group('1.5',range(7,13),'Describe all solutions of Ax = 0 in parametric vector form, where A is row equivalent to the given matrix. The displayed matrix is a coefficient matrix, not an augmented matrix.')
# Section 1.7
pairs('1.7',10,128,356,579,[(1,251,331),(3,347,407),(5,469,571),(7,586,667),(9,752,831),(11,985,1068),(13,1083,1163)])
col('1.7',10,128,579,[(10,841,924),(12,985,1068),(14,1083,1163)])
# Correct paired 9/10, 11/12 and 13/14; 9/10 occupy full rows each.
Q['1.7.9']['box']=[128,752,579,831];Q['1.7.10']['box']=[128,841,579,924]
Q['1.7.11']['box']=[128,985,350,1068];Q['1.7.12']['box']=[354,985,579,1068]
Q['1.7.13']['box']=[128,1083,350,1163];Q['1.7.14']['box']=[354,1083,579,1163]
pairs('1.7',10,601,829,1064,[(15,193,274),(17,275,352),(19,353,434)])
col('1.7',10,601,1068,[(21,493,549),(22,554,610),(23,615,672),(24,676,730),(25,735,788),(26,793,849),(27,854,911),(28,916,971),(29,1037,1068),(30,1075,1107),(31,1112,1168),(32,1173,1226)])
group('1.7',range(1,5),'Determine if the vectors are linearly independent. Justify each answer.')
group('1.7',range(5,9),'Determine if the columns of the matrix form a linearly independent set. Justify each answer.')
group('1.7',[9,10],'(a) For what values of h is v₃ in Span{v₁,v₂}? (b) For what values of h is {v₁,v₂,v₃} linearly dependent? Justify each answer.')
group('1.7',range(11,15),'Find the value(s) of h for which the vectors are linearly dependent. Justify each answer.')
group('1.7',range(15,21),'Determine by inspection whether the vectors are linearly independent. Justify each answer.')
group('1.7',range(29,33),'Describe the possible echelon forms of the matrix. Use the notation of Example 1 in Section 1.2: a filled square denotes a required nonzero pivot and * is arbitrary.')
# Section 1.8
col('1.8',11,119,574,[(1,193,286),(2,291,383),(3,441,512),(4,517,590),(5,594,647),(6,652,745),(7,749,803),(8,806,856),(9,909,984),(10,987,1080),(11,1084,1193),(12,1198,1326)])
col('1.8',11,586,1046,[(13,333,389),(14,394,450),(15,455,513),(16,517,574),(17,579,693),(18,701,1018),(19,1031,1198),(20,1202,1320)])
group('1.8',range(3,7),'With T defined by T(x) = Ax, find a vector x whose image under T is b, and determine whether x is unique.')
group('1.8',[9,10],'Find all x in ℝ⁴ mapped into the zero vector by x ↦ Ax for the given matrix A.')
group('1.8',range(13,17),'Use a rectangular coordinate system to plot u = (5,2), v = (−2,4), and their images under the given transformation T. Make a separate and reasonably large sketch for each exercise. Describe geometrically what T does to each vector x in ℝ².')
# Section 1.9
col('1.9',12,77,525,[(1,178,226),(4,281,344),(5,349,397),(6,406,455),(7,459,548),(8,551,602),(9,606,672),(10,675,726),(11,728,836),(12,839,888),(13,891,1118),(14,1121,1359)])
col('1.9',12,543,984,[(2,127,194),(3,198,244),(15,274,343),(16,351,424),(17,499,533),(18,536,572),(19,575,609),(20,613,646),(21,650,719),(22,724,793),(23,845,916),(24,920,975),(25,978,1034),(26,1038,1111),(27,1116,1185),(28,1190,1246),(29,1251,1304),(30,1308,1415)])
group('1.9',range(1,11),'Assume that T is a linear transformation. Find the standard matrix of T.')
group('1.9',[15,16],'Fill in the missing entries of the matrix, assuming that the equation holds for all values of the variables.')
group('1.9',range(17,21),'Show that T is a linear transformation by finding a matrix that implements the mapping. Note that x₁,x₂,… are entries in vectors, not vectors themselves.')
# Section 2.1
col('2.1',13,113,575,[(1,470,502),(2,504,536),(3,608,664),(4,667,764)])
col('2.1',13,586,1032,[(5,318,392),(6,395,465),(7,470,514),(8,519,548),(9,550,619),(10,621,687),(11,690,838)])
col('2.1',14,124,584,[(12,151,240),(13,245,315),(14,319,582),(15,656,707),(16,710,767),(17,770,834),(18,838,888),(19,891,924),(20,926,961),(21,963,997),(22,998,1033),(23,1035,1085),(24,1088,1139),(25,1140,1212),(26,1215,1265),(27,1268,1342)])
col('2.1',14,600,1061,[(28,153,207),(29,208,279),(30,283,335),(31,339,414),(32,416,509),(33,511,589),(34,591,640),(35,773,869),(36,871,923),(37,927,1039),(38,1041,1098),(39,1100,1150),(40,1151,1200),(41,1201,1238),(42,1239,1293),(43,1294,1343)])
group('2.1',[1,2],'Compute each matrix sum or product if it is defined. If an expression is undefined, explain why.')
for n in [1,2]:Q[f'2.1.{n}']['extra']=[[13,114,372,568,466]]
group('2.1',[5,6],'Compute AB in two ways: (a) by the definition, computing Ab₁ and Ab₂ separately; (b) by the row–column rule.')
for n in range(3,44):Q[f'2.1.{n}']['instruction']=Q[f'2.1.{n}']['instruction']+' Assume each matrix expression is defined: matrix and vector sizes match appropriately.'
group('2.1',range(15,25),'The matrices A,B,C are arbitrary and all indicated sums and products are defined. Mark the statement True or False and justify your answer.')
group('2.1',[35,36],'View u,v in ℝⁿ as n × 1 matrices. The scalar (inner) product uᵀv is a 1 × 1 matrix, usually written as a real number. The outer product uvᵀ is an n × n matrix.')
# Section 2.2
pairs('2.2',15,82,292,566,[(1,159,216),(3,222,281)])
col('2.2',15,81,567,[(5,281,317),(6,318,354),(7,355,466),(8,474,582),(9,591,881),(10,885,944)])
col('2.2',15,582,1080,[(11,187,247),(12,258,339),(13,345,408),(14,413,453),(15,457,539),(16,543,622),(17,625,710),(18,710,752),(19,755,798),(20,799,862),(21,865,944)])
col('2.2',16,82,571,[(22,93,259),(23,262,338),(24,341,394),(25,397,471),(26,474,550),(27,553,603),(28,605,659),(29,661,714),(30,715,891),(31,894,945),(32,950,1003),(33,1008,1132),(34,1137,1212),(35,1265,1388)])
col('2.2',16,592,1080,[(36,94,130),(37,237,444),(38,451,529),(43,750,959),(44,965,1144),(45,1151,1262),(46,1271,1381)])
pairs('2.2',16,592,834,1080,[(39,588,650),(41,656,743)])
group('2.2',range(1,5),'Find the inverse of the matrix.')
group('2.2',range(39,43),'Find the inverse of the matrix, if it exists. Use the algorithm introduced in this section.')
group('2.2',[35,36],'Prove Theorem 4 for A = [a,b;c,d].')
group('2.2',[37,38],'Prove these special cases of the elementary-matrix facts. Here A is a 3 × 3 matrix and I = I₃. A general proof would require more notation.')
# Shared T/F directions, with the expanded first occurrence preserved.
for sec,start,end in [('1.1',27,34),('1.2',25,34),('1.3',23,32),('1.4',23,32),('1.7',21,28),('1.9',23,30),('2.2',11,20)]:
 group(sec,range(start,end+1),'Mark each statement True or False (T/F). Justify each answer by a definition or theorem; for a false statement, explain its failure or give a counterexample.')
Q['1.1.27']['extra']=[[2,601,391,1078,619]]
# Referenced data must be present on the same card, not a separate scan page.
for sec,nums,shift in [('1.1',range(15,19),4),('1.2',range(15,19),6),('1.5',range(13,17),4)]:
 for n in nums:Q[f'{sec}.{n}']['dependencies']=[f'{sec}.{n-shift}']
for id,refs in {'1.2.6':['1.2.5'],'1.3.3':['1.3.1'],'1.3.4':['1.3.2'],'1.3.20':['1.3.16'],'1.4.16':['1.4.15'],'1.5.19':['1.5.5'],'1.5.20':['1.5.6'],'1.8.11':['1.8.9'],'1.8.12':['1.8.10'],'1.9.12':['1.9.8'],'2.2.5':['2.2.1'],'2.2.6':['2.2.2'],'2.2.7':['2.2.1'],'2.2.8':['2.2.2'],'2.2.44':['2.2.43']}.items():Q[id]['dependencies']=refs
# Verified text is added separately; original question crops remain available.
def text(id,s):Q[id]['text']=s
# Faithful mathematical transcription. Numeric arrays are read from the exact,
# previously verified manuscript, never recomputed for the display.
SRC=Path(__file__).resolve().parent.parent/'source'
work=(SRC/'MATH2255-Exercises-and-Detailed-Solutions.md').read_text()
sol={m.group(1):m.group(2) for m in re.finditer(r'^### ([\d.]+) - [^\n]+\n(.*?)(?=^### |^# |\Z)',work,re.M|re.S)}
def first(id):return json.loads(re.search(r'^@matrix (.+)$',sol[id],re.M).group(1))
def matrix(a,bar=None):return '\n\n@matrix '+json.dumps({'a':[[str(v) for v in row] for row in a],'bar':bar})+'\n\n'
def fm(id,strip=0):
 d=first(id);a=d['a'];return matrix([r[:-strip] if strip else r for r in a],None if strip else d.get('bar'))
def equations(a):
 out=[]
 for row in a:
  terms=[]
  for j,v in enumerate(row[:-1],1):
   if str(v)=='0':continue
   neg=str(v).startswith('-');coef=str(v).lstrip('-');term=('' if coef=='1' else coef+' ')+'x_'+str(j)
   terms.append((' - ' if neg else ' + ')+term)
  left=''.join(terms).strip();left=left[2:] if left.startswith('+ ') else left
  out.append('@eq '+(left or '0')+' = '+str(row[-1]))
 return '\n\n'.join(out)+'\n\n'
for n in [1,2,3,4,11,12,13,14,19,20,21,22]:
 id=f'1.1.{n}';d=first(id)
 intro=Q[id]['instruction'] or {3:'Find the point (x₁,x₂) that lies on both lines. See the figure.',4:'Find the point of intersection of the lines.',21:'Do these three lines have a common point of intersection? Explain.',22:'Do these three planes have at least one common point of intersection? Explain.'}.get(n,'Solve the system.')
 text(id,intro+'\n\n'+equations(d['a']))
for n in [7,8,9,10]:
 id=f'1.1.{n}';text(id,Q[id]['instruction']+fm(id))
text('1.1.5',Q['1.1.5']['instruction']+matrix([[1,-4,5,0,7],[0,1,-3,0,6],[0,0,1,0,2],[0,0,0,1,-5]],4))
text('1.1.6',Q['1.1.6']['instruction']+matrix([[1,-6,4,0,-1],[0,2,-7,0,4],[0,0,1,2,-3],[0,0,3,1,6]],4))
Q['1.1.3']['extra']=[[1,165,344,523,498]]
for n in range(15,19):text(f'1.1.{n}',f'Verify that the solution you found to Exercise {n-4} is correct by substituting the values you obtained back into the original equations.')
for n,a in [(23,[[1,'h',4],[3,6,8]]),(24,[[1,'h',-3],[-2,4,6]]),(25,[[1,3,-2],[-4,'h',8]]),(26,[[2,-3,'h'],[-6,9,5]])]:text(f'1.1.{n}',Q[f'1.1.{n}']['instruction']+matrix(a,2))
text('1.1.35','Find an equation involving g,h,k that makes this augmented matrix correspond to a consistent system:'+matrix([[1,-4,7,'g'],[0,3,-5,'h'],[-2,5,-9,'k']],3))
text('1.1.36','Construct three different augmented matrices for linear systems whose solution set is x₁ = −2, x₂ = 1, x₃ = 0.')
text('1.1.37','Suppose the system below is consistent for all possible values of f and g. What can you say about the coefficients c and d? Justify your answer.\n\n@eq x_1 + 3 x_2 = f\n\n@eq c x_1 + d x_2 = g')
for n in [3,4,7,8,9,10,11,12,13,14]:
 id=f'1.2.{n}';text(id,Q[id]['instruction']+fm(id))
text('1.2.5','Describe the possible echelon forms of a nonzero 2 × 2 matrix. Use the symbols ■, *, and 0, as in the first part of Example 1. Here ■ denotes a nonzero leading entry and * is arbitrary.')
text('1.2.6','Repeat Exercise 5 for a nonzero 3 × 2 matrix.')
for n in range(15,19):text(f'1.2.{n}',f'Write down the equations corresponding to the augmented matrix in Exercise {n-6} and verify that your answer to Exercise {n-6} is correct by substituting the solutions you obtained back into the original equations.')
for n,a in [(21,[[2,3,'h'],[4,6,7]]),(22,[[1,-3,-2],[5,'h',-7]])]:text(f'1.2.{n}',Q[f'1.2.{n}']['instruction']+matrix(a,2))
text('1.2.23',Q['1.2.23']['instruction']+'\n\n@eq x_1 + h x_2 = 2\n\n@eq 4 x_1 + 8 x_2 = k')
text('1.2.24',Q['1.2.24']['instruction']+'\n\n@eq x_1 + 3 x_2 = 2\n\n@eq 3 x_1 + h x_2 = k')
for n,u,v in [(1,[-1,2],[-3,3]),(2,[3,2],[2,3])]:text(f'1.3.{n}','Compute u + v and u − 2v.\n\nu ='+matrix([[x] for x in u])+'v ='+matrix([[x] for x in v]))
for n in [3,4]:text(f'1.3.{n}',Q[f'1.3.{n}']['instruction']+f'\n\nu and v as in Exercise {n-2}; their given values are reproduced below.')
for n,a in [(9,[[0,1,5,0],[4,6,-1,0],[-1,3,-8,0]]),(10,[[4,1,3,9],[1,-7,-2,2],[8,6,-5,15]])]:text(f'1.3.{n}',Q[f'1.3.{n}']['instruction']+'\n\n'+equations(a))
for n in [11,12,13,14]:
 id=f'1.3.{n}';a=first(id)['a'];intro=Q[id]['instruction'];matname='[a₁ a₂ a₃]' if n<13 else 'A'
 text(id,intro+'\n\n'+matname+' ='+matrix([r[:-1] for r in a])+'b ='+matrix([[r[-1]] for r in a]))
for n,u,v in [(15,[7,1,-6],[-5,3,0]),(16,[3,0,2],[-2,0,3])]:text(f'1.3.{n}',Q[f'1.3.{n}']['instruction']+'\n\nv₁ ='+matrix([[x] for x in u])+'v₂ ='+matrix([[x] for x in v]))
text('1.3.20','Give a geometric description of Span{v₁,v₂} for the vectors in Exercise 16.')
for n in [11,12]:
 id=f'1.4.{n}';a=first(id)['a'];text(id,Q[id]['instruction']+'\n\nA ='+matrix([r[:-1] for r in a])+'b ='+matrix([[r[-1]] for r in a]))
for n in range(1,13):
 id=f'1.5.{n}';a=first(id)['a'];text(id,Q[id]['instruction']+'\n\n'+(equations(a) if n<7 else matrix([r[:-1] for r in a])))
for n in range(13,17):text(f'1.5.{n}',f'Verify that the solutions you found to Exercise {n-4} are indeed homogeneous solutions.')
for n in range(1,9):
 id=f'1.7.{n}';a=first(id)['a'];text(id,Q[id]['instruction']+'\n\n'+('The given vectors are the columns of:\n\n' if n<5 else '')+matrix([r[:-1] for r in a]))
for n in [3,4,5,6]:
 id=f'1.8.{n}';a=first(id)['a'];text(id,Q[id]['instruction']+'\n\nA ='+matrix([r[:-1] for r in a])+'b ='+matrix([[r[-1]] for r in a]))
for n,a in [(13,[[-1,0],[0,-1]]),(14,[['1/2',0],[0,'1/2']]),(15,[[0,0],[0,1]]),(16,[[0,1],[1,0]])]:text(f'1.8.{n}',Q[f'1.8.{n}']['instruction']+'\n\n@eq T(x) = A x\n\nA ='+matrix(a)+'The source decimal .5 in Exercise 14 is exactly 1/2.') if n==14 else text(f'1.8.{n}',Q[f'1.8.{n}']['instruction']+'\n\n@eq T(x) = A x\n\nA ='+matrix(a))
text('1.9.14','Let T: ℝ² → ℝ² be a linear transformation with standard matrix A = [a₁ a₂], where a₁ and a₂ are shown in the figure. Using the figure, draw the image of (−1,3) under the transformation T.')
Q['1.9.14']['extra']=[[12,232,1225,421,1355]]
for n,a in [(1,[[8,3],[5,2]]),(2,[[3,1],[7,2]]),(3,[[8,3],[-7,-3]]),(4,[[3,-2],[7,-4]]),(39,[[1,2],[4,7]]),(40,[[5,10],[4,7]]),(41,[[1,0,-2],[-3,1,4],[2,-3,4]]),(42,[[1,-2,1],[4,-7,3],[-2,6,-4]])]:text(f'2.2.{n}',Q[f'2.2.{n}']['instruction']+matrix(a))
for n in [5,6]:text(f'2.2.{n}',f'Verify that the inverse you found in Exercise {n-4} is correct.')
for n in [7,8]:text(f'2.2.{n}',f'Use the inverse found in Exercise {n-6} to solve the system.\n\n'+equations(first(f'2.2.{n}')['a']))
text('2.2.9','Let A = [1,2;5,12], b₁ = (−1,3), b₂ = (1,−5), b₃ = (2,6), and b₄ = (3,5).\n\n(a) Find A^(-1) and use it to solve the four equations Ax = b₁, Ax = b₂, Ax = b₃, and Ax = b₄.\n\n(b) The four equations in part (a) can be solved by the same set of row operations, since the coefficient matrix is the same in each case. Solve the four equations in part (a) by row reducing the augmented matrix [A b₁ b₂ b₃ b₄].')
text('2.2.45','Let A = [−2,−7,−9;2,5,6;1,3,4]. Find the third column of A^(-1) without computing the other columns.')
text('2.2.46','Let A = [−25,−9,−27;546,180,537;154,50,149]. Find the second and third columns of A^(-1) without computing the first column.')
# Transcribed T/F claims retain the full proposition, not the solution title.
def claims(sec,start,lines):
 for n,line in enumerate(lines.strip().split('\n'),start):text(f'{sec}.{n}','Mark this statement True or False. Justify your answer.\n\n'+line)
claims('1.1',27,'''Every elementary row operation is reversible.
Elementary row operations on an augmented matrix never change the solution set of the associated linear system.
A 5 × 6 matrix has six rows.
Two matrices are row equivalent if they have the same number of rows.
The solution set of a linear system involving variables x₁,…,xₙ is a list of numbers (s₁,…,sₙ) that makes each equation in the system a true statement when the values s₁,…,sₙ are substituted for x₁,…,xₙ, respectively.
An inconsistent system has more than one solution.
Two fundamental questions about a linear system involve existence and uniqueness.
Two linear systems are equivalent if they have the same solution set.''')
claims('1.2',25,'''In some cases, a matrix may be row reduced to more than one matrix in reduced echelon form, using different sequences of row operations.
The echelon form of a matrix is unique.
The row reduction algorithm applies only to augmented matrices for a linear system.
The pivot positions in a matrix depend on whether row interchanges are used in the row reduction process.
A basic variable in a linear system is a variable that corresponds to a pivot column in the coefficient matrix.
Reducing a matrix to echelon form is called the forward phase of the row reduction process.
Finding a parametric description of the solution set of a linear system is the same as solving the system.
Whenever a system has free variables, the solution set contains a unique solution.
If one row in an echelon form of an augmented matrix is [0 0 0 0 5], then the associated linear system is inconsistent.
A general solution of a system is an explicit description of all solutions of the system.''')
claims('1.7',21,'''The columns of a matrix A are linearly independent if the equation Ax = 0 has the trivial solution.
Two vectors are linearly dependent if and only if they lie on a line through the origin.
If S is a linearly dependent set, then each vector is a linear combination of the other vectors in S.
If a set contains fewer vectors than there are entries in the vectors, then the set is linearly independent.
The columns of any 4 × 5 matrix are linearly dependent.
If x and y are linearly independent, and if z is in Span{x,y}, then {x,y,z} is linearly dependent.
If x and y are linearly independent, and if {x,y,z} is linearly dependent, then z is in Span{x,y}.
If a set in ℝⁿ is linearly dependent, then the set contains more vectors than there are entries in each vector.''')
# Source truncation is explicit; the visible text is not treated as an executable instruction.
text('1.2.41','**Incomplete original statement.** The supplied scan ends after: “A system of linear equations with fewer equations than unknowns is sometimes called an underdetermined system.” The question continuation is missing. No missing request is inferred.')
text('2.1.43','**Incomplete original statement.** The supplied scan reads: “Use a web search engine such as Google to find documentation for your matrix program, and write the commands that” and then cuts off. The required commands or operations are not supplied. No continuation is invented.')
claims('1.3',23,'''Another notation for the column vector (−4,3) is the horizontal row matrix [−4 3].
Any list of five real numbers is a vector in ℝ⁵.
The points in the plane corresponding to (−2,5) and (−5,2) lie on a line through the origin.
The vector u results when a vector u − v is added to the vector v.
An example of a linear combination of vectors v₁ and v₂ is the vector (1/2)v₁.
The weights c₁,…,cₚ in a linear combination c₁v₁ + … + cₚvₚ cannot all be zero.
The solution set of the linear system whose augmented matrix is [a₁ a₂ a₃ b] is the same as the solution set of the equation x₁a₁ + x₂a₂ + x₃a₃ = b.
When u and v are nonzero vectors, Span{u,v} contains the line through u and the origin.
The set Span{u,v} is always visualized as a plane through the origin.
Asking whether the linear system corresponding to an augmented matrix [a₁ a₂ a₃ b] has a solution amounts to asking whether b is in Span{a₁,a₂,a₃}.''')
claims('1.4',23,'''The equation Ax = b is referred to as a vector equation.
Every matrix equation Ax = b corresponds to a vector equation with the same solution set.
If the equation Ax = b is inconsistent, then b is not in the set spanned by the columns of A.
A vector b is a linear combination of the columns of a matrix A if and only if the equation Ax = b has at least one solution.
The equation Ax = b is consistent if the augmented matrix [A b] has a pivot position in every row.
If A is an m × n matrix whose columns do not span ℝᵐ, then the equation Ax = b is inconsistent for some b in ℝᵐ.
The first entry in the product Ax is a sum of products.
Any linear combination of vectors can always be written in the form Ax for a suitable matrix A and vector x.
If the columns of an m × n matrix A span ℝᵐ, then the equation Ax = b is consistent for each b in ℝᵐ.
The solution set of a linear system whose augmented matrix is [a₁ a₂ a₃ b] is the same as the solution set of Ax = b, if A = [a₁ a₂ a₃].''')
claims('1.9',23,'''A linear transformation T: ℝⁿ → ℝᵐ is completely determined by its effect on the columns of the n × n identity matrix.
A mapping T: ℝⁿ → ℝᵐ is one-to-one if each vector in ℝⁿ maps onto a unique vector in ℝᵐ.
If T: ℝ² → ℝ² rotates vectors about the origin through an angle φ, then T is a linear transformation.
The columns of the standard matrix for a linear transformation from ℝⁿ to ℝᵐ are the images of the columns of the n × n identity matrix.
When two linear transformations are performed one after another, then the combined effect may not always be a linear transformation.
Not every linear transformation from ℝⁿ to ℝᵐ is a matrix transformation.
A mapping T: ℝⁿ → ℝᵐ is onto ℝᵐ if every vector x in ℝⁿ maps onto some vector in ℝᵐ.
The standard matrix of a linear transformation from ℝ² to ℝ² that reflects points through the horizontal axis, the vertical axis, or the origin has the form [a,0;0,d], where a and d are ±1.''')
claims('2.1',15,'''If A and B are 2 × 2 with columns a₁,a₂ and b₁,b₂, respectively, then AB = [a₁b₁ a₂b₂].
If A and B are 3 × 3 and B = [b₁ b₂ b₃], then AB = [Ab₁ + Ab₂ + Ab₃].
Each column of AB is a linear combination of the columns of B using weights from the corresponding column of A.
The second row of AB is the second row of A multiplied on the right by B.
AB + AC = A(B + C).
A^T + B^T = (A + B)^T.
(AB)C = (AC)B.
(AB)^T = A^T B^T.
The transpose of a product of matrices equals the product of their transposes in the same order.
The transpose of a sum of matrices equals the sum of their transposes.''')
claims('2.2',11,'''In order for a matrix B to be the inverse of A, both equations AB = I and BA = I must be true.
A product of invertible n × n matrices is invertible, and the inverse of the product is the product of their inverses in the same order.
If A and B are n × n and invertible, then A^(-1)B^(-1) is the inverse of AB.
If A is invertible, then the inverse of A^(-1) is A itself.
If A = [a,b;c,d] and ab − cd ≠ 0, then A is invertible.
If A = [a,b;c,d] and ad = bc, then A is not invertible.
If A is an invertible n × n matrix, then the equation Ax = b is consistent for each b in ℝⁿ.
If A can be row reduced to the identity matrix, then A must be invertible.
Each elementary matrix is invertible.
If A is invertible, the elementary row operations that reduce A to the identity Iₙ also reduce A^(-1) to Iₙ.''')
for n,s in {35:'Suppose a 3 × 5 coefficient matrix for a system has three pivot columns. Is the system consistent? Why or why not?',36:'Suppose a system of linear equations has a 3 × 5 augmented matrix whose fifth column is a pivot column. Is the system consistent? Why or why not?',37:'Suppose the coefficient matrix of a system of linear equations has a pivot position in every row. Explain why the system is consistent.',38:'Suppose the coefficient matrix of a linear system of three equations in three variables has a pivot in each column. Explain why the system has a unique solution.',39:'Restate the last sentence in Theorem 2 using the concept of pivot columns: “If a linear system is consistent, then the solution is unique if and only if ______.”',40:'What would you have to know about the pivot columns in an augmented matrix in order to know that the linear system is consistent and has a unique solution?'}.items():text(f'1.2.{n}',s)
# Export the final reviewed question index.
if __name__=='__main__':
 (Path(__file__).parent/'question-index.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2))
 print('Final:',sum('text' in q for q in Q.values()),'verified transcriptions')
