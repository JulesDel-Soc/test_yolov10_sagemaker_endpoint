import numpy as np
import torch, os, json, base64, cv2, time
from ultralytics import YOLOv10

def model_fn(model_dir):
    print("Executing model_fn from inference.py ...")
    env = os.environ
    model = YOLOv10(os.path.join(model_dir, env['YOLOV10_MODEL']))
    return model

def input_fn(request_body, request_content_type):
    print("Executing input_fn from inference.py ...")
    if request_content_type:
        jpg_original = base64.b64decode(request_body)
        jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
        img = cv2.imdecode(jpg_as_np, flags=-1)
    else:
        raise Exception("Unsupported content type: " + request_content_type)
    return img
    
def predict_fn(input_data, model):
    print("Executing predict_fn from inference.py ...")
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    with torch.no_grad():
        result = model(input_data)
    return result
        
def output_fn(prediction_output, content_type):
    print("Executing output_fn from inference.py ...")
    result = prediction_output[0]
    json_result = result.to_json()
    try:
        return json_result
    except Exception as e:
        print(e)
        raise esult.probs.cpu().numpy().data.tolist()
    return json.dumps(infer)