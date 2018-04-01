////
////  JsonParse.swift
////  Quizzical
////
////  Created by Rucha Patki on 4/1/18.
////  Copyright © 2018 ruchapatki. All rights reserved.
////
//
//import UIKit
//
//struct Info: Decodable {
//    let Question: String
//    let Correct: String
//    let Answers: [String]
//}
//
//struct Idk: Decodable {
//    let response: [Info]
//}
//
//class JsonParse: UIViewController {
//
//    var question: [String] = []
//    var correct: [String] = []
//    var answers: [[String]] = []
//
//    override func viewDidLoad() {
//        super.viewDidLoad()
//
//
//        let jsonUrlString = "https://quizzical-199802.appspot.com/"
//        let url = URL(string:jsonUrlString)
//
//        URLSession.shared.dataTask(with: url!) {(data, response, error) in
//            do {
//                var infos = try JSONDecoder().decode([Info].self, from: data!)
//
//                var i = 0;
//                while i < infos.count{
//                    self.question.append(infos[i].Question)
//                    self.correct.append(infos[i].Correct)
//                    var j = 0;
//                    var ansSet: [String] = []
//                    while j < infos[i].Answers.count {
//                        ansSet.append(infos[i].Answers[j])
//                        j += 1
//                    }
//                    self.answers.append(ansSet)
//                    i += 1
//                }
//                print(self.question)
//            } catch {
//                print("Error", error)
//            }
//        }.resume()
//
//
////local
////        let path = Bundle.main.path(forResource: "stuff", ofType: "json")
////        let url = URL(fileURLWithPath: path!)
////
////        do{
////            let data = try Data(contentsOf: url)
////            let stuff = try JSONDecoder().decode([Info].self, from: data)
////
////            var i = 0;
////            while i < stuff.count{
////                question.append(stuff[i].Question)
////                correct.append(stuff[i].Correct)
////                var j = 0;
////                var ansSet: [String] = []
////                while j < stuff[i].Answers.count {
////                    ansSet.append(stuff[i].Answers[j])
////                    j += 1
////                }
////                answers.append(ansSet)
////                i += 1
////            }
////        }
////        catch{}
//
//    }
//}
//
