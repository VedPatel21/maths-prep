import Foundation
import Vision
import AppKit
var result: [String:Any] = [:]
for arg in CommandLine.arguments.dropFirst() {
 let url=URL(fileURLWithPath:arg)
 let req=VNRecognizeTextRequest()
 req.recognitionLevel = .accurate
 req.usesLanguageCorrection = false
 try VNImageRequestHandler(url:url).perform([req])
 result[url.lastPathComponent] = req.results!.map { r in ["text":r.topCandidates(1).first!.string,"x":r.boundingBox.minX,"y":1-r.boundingBox.maxY,"w":r.boundingBox.width,"h":r.boundingBox.height] as [String:Any] }
}
let d=try JSONSerialization.data(withJSONObject:result,options:[.prettyPrinted,.sortedKeys]);print(String(data:d,encoding:.utf8)!)
