import Alamofire

func uploadImage(image: UIImage) {
    guard let imageData = image.jpegData(compressionQuality: 1.0) else { return }
    
    let url = "http://47.103.61.134:4050/upload" // 假设这是上传接口
    AF.upload(multipartFormData: { multipartFormData in
        multipartFormData.append(imageData, withName: "file", fileName: "image.jpg", mimeType: "image/jpeg")
    }, to: url).responseJSON { response in
        switch response.result {
        case .success(let value):
            print("上传成功：\(value)")
        case .failure(let error):
            print("上传失败：\(error)")
        }
    }
}
