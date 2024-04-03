import time
import logging
from datetime import datetime 
import os
def to_do_logic(
    param_json: dict = None,
    ex_model_param: dict = None,
    in_dir: str = None,
    out_dir: str = None,
    ex_out_dir: str = None,
    is_training: bool = False,
    training_model_path: str = None,
) :

    accuracy_json: dict = {}
    loss_json: dict = {}
    output_params: dict = {}
    files: list = list()

    # 로고 파일 생성
    logging.basicConfig(filename=f'{out_dir}{os.sep}log_file.txt', level=logging.DEBUG,
                    format="[ %(asctime)s | %(levelname)s ] %(message)s", force=True,
                    datefmt="%Y-%m-%d %H:%M:%S")
    files.append("log_file.txt")
    logger = logging.getLogger()

    logging.info("##################################################")
    logging.info(f"param_json => {param_json}")    
    logging.info(f"ex_model_param => {ex_model_param}")    
    logging.info(f"in_dir => {in_dir}")    
    logging.info(f"out_dir => {out_dir}")    
    logging.info(f"ex_out_dir => {ex_out_dir}")    
    logging.info(f"is_training => {is_training}")    
    logging.info(f"training_model_path => {training_model_path}")    
    logging.info("##################################################")
    
  
    for key in param_json:
        value = param_json[key]
        if isinstance(value, int):
            value = value * 3
        elif isinstance(value, str):
            value = value + "_tail"
        param_json[key] = value
        
    param_json['now'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return accuracy_json, loss_json, output_params, files

if __name__ == "__main__":
    print("model starts running")
    t1 , t2, output, t3 = to_do_logic(
        param_json = {'a' : 10, 'b': 'wow'}
    )
    print(output)
