//
//  ClientModel.swift
//  image_host_client
//
//  Created by 李灿晨 on 10/28/19.
//  Copyright © 2019 李灿晨. All rights reserved.
//

import Cocoa
import Alamofire

class ClientModel: NSObject {
    
    private var backendURLString: String!
    private var backendToken: String!
    
    init(backendURLString: String, backendToken: String) {
        self.backendURLString = backendURLString
        self.backendToken = backendToken
    }
    
    /**
     Send a file to the backend, copy the direct link to clipboard if success.
     
     - Parameters:
        - url: The URL of the file to be sent.
        - quality: The compress quality for images. 0 to 100, the bigger `quality` is, the better quality
            the image is.
        - completion: The completion handler. The `String` parameter would be the direct link if there
            is no error.
     */
    func sendFile(url: URL, quality: Int, completion: ((String?, Error?) -> ())?) {
        var imageData: Data? = nil
        do {
            imageData = try Data(contentsOf: url)
        } catch {
            print(error)
            completion?(nil, InputError.fileNotFound)
            return
        }
        Alamofire.upload(
            multipartFormData: { multipartFormData in
                multipartFormData.append(imageData!, withName: "image", fileName: "image.jpg", mimeType: "image/jpg")
                multipartFormData.append(String(quality).data(using: .utf8)!, withName: "compress_quality")
                multipartFormData.append(self.backendToken.data(using: .utf8)!, withName: "token")
            },
            to: backendURLString,
            encodingCompletion: { encodingResult in
                switch encodingResult {
                case .success(let upload, _, _):
                    upload.responseData() { dataResponse in
                        guard dataResponse.data != nil else {completion?(nil, BackendError.unexpectedResponse);return}
                        completion?(String(data: dataResponse.data!, encoding: .utf8)!, nil)
                        self.sendToPasteboard(String(data: dataResponse.data!, encoding: .utf8)!)
                    }
                case .failure(let encodingError):
                    completion?(nil, encodingError)
                }
            }
        )
    }
    
    /**
     Set the `backendURLString` to the given value.
     */
    func setBackendURLString(_ item: String) {
        self.backendURLString = item
    }
    
    /**
     Set the `backendToken` to the given value.
     */
    func setBackendToken(_ item: String) {
        self.backendToken = item
    }
    
    /**
     Send `item` to system clipboard.
     
     - Parameters:
        - item: The string item to be sent to the system clipboard.
     */
    private func sendToPasteboard(_ item: String) {
        let pasteboard = NSPasteboard()
        pasteboard.declareTypes([.string], owner: nil)
        pasteboard.setString(item, forType: .string)
    }
    
}
