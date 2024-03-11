import time
import logging

def to_do_logic(
    param_json: dict = None,
    ex_model_param: dict = None,
    in_dir: str = None,
    out_dir: str = None,
    ex_out_dir: str = None,
    is_training: bool = False,
    training_model_path: str = None,
) :
    logging.info("##################################################")
    logging.info(f"param_json => {param_json}")    
    logging.info(f"ex_model_param => {ex_model_param}")    
    logging.info(f"in_dir => {in_dir}")    
    logging.info(f"out_dir => {out_dir}")    
    logging.info(f"ex_out_dir => {ex_out_dir}")    
    logging.info(f"is_training => {is_training}")    
    logging.info(f"training_model_path => {training_model_path}")    
    logging.info("##################################################")
    
    # for i in range(60):
    #     logging.info(f"Step {i}")
    #     time.sleep(1)
    b = 10 / 0
    accuracy_json = {'a' : 100}
    loss_json = {'b' : 80}
    output_params = {'p1' : 'x', 'p2' : 'y', 'p3' : 10}
    files = []
    return accuracy_json, loss_json, output_params, files

if __name__ == "__main__":
    logging.info("model starts running")
    for i in range(300):
        logging.info(f"Step {i}")
        time.sleep(1)
