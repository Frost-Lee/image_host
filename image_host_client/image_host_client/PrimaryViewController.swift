//
//  ViewController.swift
//  image_host_client
//
//  Created by 李灿晨 on 10/28/19.
//  Copyright © 2019 李灿晨. All rights reserved.
//

import Cocoa

class PrimaryViewController: NSViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let model = ClientModel(
            backendURLString: "http://144.202.103.127:1910/bloghost",
            backendToken: "hcuygaukhhrzyriu"
        )
        model.sendFile(url: URL(fileURLWithPath: "/Users/Frost/Desktop/IMG_0639.jpeg"), quality: 50) { message, error in
            print(message)
            print(error)
        }
        
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}

