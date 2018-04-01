//
//  PhotoVC.swift
//  Quizzical
//
//  Created by Rucha Patki on 3/31/18.
//  Copyright © 2018 ruchapatki. All rights reserved.
//

import UIKit
import Firebase


class PhotoVC: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var quizButton: UIButton!
    @IBOutlet weak var selectImgBtn: UIButton!
    
    
    var myImg: UIImage!
    
    let imagePicker = UIImagePickerController()
    

    override func viewDidLoad() {
        super.viewDidLoad()
        imagePicker.delegate = self
        quizButton.isEnabled = false
        quizButton.layer.cornerRadius = 10
        
    }

    @IBAction func selectPhoto(_ sender: Any) {
        quizButton.isEnabled = false
        imagePicker.allowsEditing = false
        imagePicker.sourceType = .photoLibrary
        present(imagePicker,animated:true, completion:nil)
    }
    
    @IBAction func quizClicked(_ sender: Any) {
        storageWrite()
    }
    
}


extension PhotoVC: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        dismiss(animated: true, completion: nil)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        let image = info[UIImagePickerControllerOriginalImage] as? UIImage
        myImg = image
        imageView.image = image
        imageView.layer.borderWidth = 0
        dismiss(animated: true, completion: nil)
        quizButton.isEnabled = true
    }
    
    func storageWrite(){
        var storageRef = Storage.storage().reference().child("images/image.png")
        let data = UIImagePNGRepresentation(myImg)
        let metadata = StorageMetadata()
        metadata.contentType = "image/png"
        let uploadTask = storageRef.putData(data!, metadata: metadata)
    }
 
}

extension UIView {
    func roundCorners(corners:UIRectCorner, radius: CGFloat) {
        let path = UIBezierPath(roundedRect: self.bounds, byRoundingCorners: corners, cornerRadii: CGSize(width: radius, height: radius))
        let mask = CAShapeLayer()
        mask.path = path.cgPath
        self.layer.mask = mask
    }
}
extension UIButton{
    func roundedButton(){
        let size = CGSize(width: 8.0, height: 8.0)
        let maskPAth1 = UIBezierPath(roundedRect: self.bounds,
                                     byRoundingCorners: [.bottomLeft , .bottomRight],
                                     cornerRadii:size)
        let maskLayer1 = CAShapeLayer()
        maskLayer1.frame = self.bounds
        maskLayer1.path = maskPAth1.cgPath
        self.layer.mask = maskLayer1
        
    }
}
