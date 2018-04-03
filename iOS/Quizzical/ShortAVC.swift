//
//  ShortAVC.swift
//  Quizzical
//
//  Created by Rucha Patki on 3/31/18.
//  Copyright © 2018 ruchapatki. All rights reserved.
//

import UIKit

class ShortAVC: UIViewController {
    
    var counter = 1;
    
    @IBOutlet weak var qNum: UILabel!
    @IBOutlet weak var questionBox: UITextView!
    @IBOutlet weak var submitAns: UIButton!
    @IBOutlet weak var answerField: UITextView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        answerField.isEditable = true
        answerField.layer.masksToBounds = true
        answerField.layer.cornerRadius = 10
        qNum.layer.masksToBounds = true
        qNum.layer.cornerRadius = 20
        questionBox.isEditable = false
        updateQuestion(questions: question)
    }
    
    func updateQuestion(questions: [String]){
        let myColor = UIColor(red: 43/255, green: 33/255, blue: 49/255, alpha: 1)
        
        qNum.text = "Question \(questionIndex+1)"
//        let questionText = "\(question[questionIndex])"
        let questionText = "\(question[question.count - counter])"
        questionBox.text = questionText
        answerField.text = ""
    }
    
    
    @IBAction func submitPressed(_ sender: Any) {
//        if(questionIndex < 12){ //NOTE
//            questionIndex+=1
//            updateQuestion(questions: question)
//        }
        if(counter < 3) {
            counter += 1
            updateQuestion(questions: question)
            questionIndex += 1
        }
        else{
            performSegue(withIdentifier: "toScore", sender: nil)
        }
    }
}
