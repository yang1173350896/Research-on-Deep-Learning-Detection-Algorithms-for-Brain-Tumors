import torch
import torch.nn
import cv2
import numpy as np
import Unet

# input_dir = './input/ori118.jpg'
# output_dir = "./output/out118.jpg"
def load_net(model_dir,device = 'cuda'):
    net = Unet.UNet()
    net.to(device = device)
    net.load_state_dict(torch.load(model_dir, map_location=device))
    return net
def predict(tensor_img,net,device = 'cuda'):
    net.eval()
    with torch.no_grad():
        predict = net(tensor_img)
        pre_ = torch.sigmoid(predict)
        pre_np = pre_.to(device="cpu").detach().numpy()
    return pre_np
def transform(ori_img,device = 'cuda'):
    ori_img = ori_img/ori_img.max()
    ori_img = np.expand_dims(ori_img, axis=0)
    ori_img = np.expand_dims(ori_img, axis=0)
    img_ = torch.from_numpy(ori_img).type(torch.FloatTensor)
    tensor_img = img_.to(device=device, dtype=torch.float32)
    return tensor_img
def predict_picture(input_dir,filename):
    ori_img = cv2.imread(input_dir,0) #240 240
    model_dir = "./net/new_epoch.pth"
    output_dir ="./static/images/output/"+filename
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = load_net(model_dir,device)
    net = net.eval()
    ten_img = transform(ori_img,device)
    pre_np = predict(ten_img,net,device)
    out_pre = np.array(pre_np>0.5,dtype = np.float16) * 255
    out_pre = np.squeeze(out_pre,0)
    out_pre = np.transpose(out_pre,(1,2,0))
    out_pre = out_pre.astype(np.uint8)
    cv2.imwrite(output_dir,out_pre)
    return output_dir
















