//
//  Errors.swift
//  image_host_client
//
//  Created by 李灿晨 on 10/28/19.
//  Copyright © 2019 李灿晨. All rights reserved.
//

import Foundation

enum InputError: Error {
    case fileNotFound
    case unsupportedFormat
}

enum BackendError: Error {
    case unexpectedResponse
}
