//
//  ScoreVC.swift
//  Quizzical
//
//  Created by Rucha Patki on 3/31/18.
//  Copyright © 2018 ruchapatki. All rights reserved.
//

import UIKit

class ScoreVC: UIViewController {
    
    @IBOutlet weak var scoreBox: UILabel!
    @IBOutlet weak var messageBox: UILabel!
    
    var myQuiz: QuizVC = QuizVC()
    var myScore = score
    var myTotal = total
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        scoreBox.text = "\(myScore)/\(myTotal)"
        var totalScore = Double(myScore)/Double(myTotal)
        if(totalScore == 1){
            messageBox.text = "Amazing job! Perfect Score!"
        }
        else if(totalScore == 0){
            messageBox.text = "Looks like you have some more studying to do!"
        }
        else {
            messageBox.text = "You can do better! Take another quiz!"
        }
    }
    
    @IBAction func startingOver(_ sender: Any) {
        question = []
        correct = []
        answers = []
    }
    
    
}
