//
//  QuizVC.swift
//  Quizzical
//
//  Created by Rucha Patki on 3/31/18.
//  Copyright © 2018 ruchapatki. All rights reserved.
//

import UIKit
import QuartzCore
import Alamofire

var score = 0;
var total = 0;
var questionIndex = 0;

var question: [String] = []
var correct: [String] = []
var answers: [[String]] = []


struct Info: Decodable {
    let Question: String
    let Correct: String
    let Answers: [String]
}

class QuizVC: UIViewController {

    @IBOutlet weak var qNum: UILabel!
    @IBOutlet weak var arrow: UIButton!
    @IBOutlet weak var questionBox: UITextView!


    @IBOutlet weak var answer1: UIButton!
    @IBOutlet weak var answer2: UIButton!
    @IBOutlet weak var answer3: UIButton!
    @IBOutlet weak var answer4: UIButton!


    var correctTag = 0;

    override func viewDidLoad() {
        super.viewDidLoad()

        qNum.layer.masksToBounds = true
        qNum.layer.cornerRadius = 20
        questionBox.isEditable = false

        answer1.layer.masksToBounds = true
        answer2.layer.masksToBounds = true
        answer3.layer.masksToBounds = true
        answer4.layer.masksToBounds = true
        answer1.layer.cornerRadius = 5
        answer2.layer.cornerRadius = 5
        answer3.layer.cornerRadius = 5
        answer4.layer.cornerRadius = 5

        arrow.isHidden = true
        arrow.isEnabled = false

        score = 0;
        total = 0;
        questionIndex = 0;

        parseJSON(completion:{
            DispatchQueue.main.async(execute:{
                self.updateQuestion(questions: question, answers: answers, correct: correct)
                print(question)
                total = 6; //NOTE
            });
            
        })
    }
    

    func updateQuestion(questions: [String], answers: [[String]], correct: [String]){
        let myColor = UIColor(red: 43/255, green: 33/255, blue: 49/255, alpha: 1)
        arrow.isHidden = true;
        arrow.isEnabled = false;

        answer1.isEnabled = true
        answer2.isEnabled = true
        answer3.isEnabled = true
        answer4.isEnabled = true

        answer1.backgroundColor = myColor
        answer2.backgroundColor = myColor
        answer3.backgroundColor = myColor
        answer4.backgroundColor = myColor

        qNum.text = "Question \(questionIndex+1)"

        let questionText = question[questionIndex]
        questionBox.text = questionText

        let randomNum:UInt32 = arc4random_uniform(4)+1 //random 1-4
        var answerOne = "";
        var answerTwo = "";
        var answerThree = "";
        var answerFour = "";
        switch(randomNum){
        case 1:
            answerOne = correct[questionIndex]
            answerTwo = answers[questionIndex][0]
            answerThree = answers[questionIndex][1]
            answerFour = answers[questionIndex][2]
        case 2:
            answerTwo = correct[questionIndex]
            answerOne = answers[questionIndex][0]
            answerThree = answers[questionIndex][1]
            answerFour = answers[questionIndex][2]
        case 3:
            answerThree = correct[questionIndex]
            answerOne = answers[questionIndex][0]
            answerTwo = answers[questionIndex][1]
            answerFour = answers[questionIndex][2]
        default:
            answerFour = correct[questionIndex]
            answerOne = answers[questionIndex][0]
            answerTwo = answers[questionIndex][1]
            answerThree = answers[questionIndex][2]
        }

        answer1.setTitle("   \(answerOne)", for: .normal)
        answer2.setTitle("   \(answerTwo)", for: .normal)
        answer3.setTitle("   \(answerThree)", for: .normal)
        answer4.setTitle("   \(answerFour)", for: .normal)

        correctTag = Int(randomNum);
    }

    @IBAction func answerClicked(_ sender: UIButton) {
        let myGreen = UIColor(red: 0, green: 1, blue: 0, alpha: 0.5)
        let myRed = UIColor(red: 1, green: 0, blue: 0, alpha: 0.5)
        if(sender.tag == correctTag){

            sender.backgroundColor = myGreen
            arrow.isHidden = false
            arrow.isEnabled = true
            score += 1;

            answer1.isEnabled = false
            answer2.isEnabled = false
            answer3.isEnabled = false
            answer4.isEnabled = false
        }
        else{
            sender.backgroundColor = myRed
            if let button = self.view.viewWithTag(correctTag) as? UIButton
            {
                button.backgroundColor = myGreen
            }
            arrow.isHidden = false
            arrow.isEnabled = true

            answer1.isEnabled = false
            answer2.isEnabled = false
            answer3.isEnabled = false
            answer4.isEnabled = false
        }
    }


    @IBAction func arrowClicked(_ sender: Any) {
        if(questionIndex < 5){ //NOTE
            questionIndex+=1
            updateQuestion(questions: question, answers: answers, correct: correct)
        }
        else{
            questionIndex+=1
            performSegue(withIdentifier: "toShort", sender: nil)
        }
    }

    func parseJSON(completion: @escaping () ->()){
        
        let jsonUrlString = "https://quizzical-199802.appspot.com/"
        let url = URL(string:jsonUrlString)
        var urlRequest = URLRequest(url: url!)
        urlRequest.httpMethod = "GET"

        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)

        let myData = session.dataTask(with: urlRequest) {(data, response, error) in
            do {
                var infos = try JSONDecoder().decode([Info].self, from: data!)

                var i = 0;
                while i < infos.count{
                    question.append(infos[i].Question)
                    correct.append(infos[i].Correct)
                    var j = 0;
                    var ansSet: [String] = []
                    while j < infos[i].Answers.count {
                        ansSet.append(infos[i].Answers[j])
                        j += 1
                    }
                    answers.append(ansSet)
                    i += 1
                }
                print(question)
            } catch {
                print("Error", error)
            }
            completion()
        }
        myData.resume()
        
//local
//        let path = Bundle.main.path(forResource: "stuff", ofType: "json")
//        let url = URL(fileURLWithPath: path!)
//
//        do{
//            let data = try Data(contentsOf: url)
//            let stuff = try JSONDecoder().decode([Info].self, from: data)
//
//            var i = 0;
//            while i < stuff.count{
//                question.append(stuff[i].Question)
//                correct.append(stuff[i].Correct)
//                var j = 0;
//                var ansSet: [String] = []
//                while j < stuff[i].Answers.count {
//                    ansSet.append(stuff[i].Answers[j])
//                    j += 1
//                }
//                answers.append(ansSet)
//                i += 1
//            }
//        }
//        catch{}
    }

}


