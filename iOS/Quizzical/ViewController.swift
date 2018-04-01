//
//  ViewController.swift
//  Quizzical
//
//  Created by Rucha Patki on 3/31/18.
//  Copyright © 2018 ruchapatki. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var getStarted: UIButton!

    //if time: change highlight when scrolled over
    override func viewDidLoad() {
        let myColor = UIColor(red: 177/255, green: 137/255, blue: 200/255, alpha: 1)
        getStarted.layer.borderColor = myColor.cgColor
        getStarted.layer.borderWidth = 1
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    


}

