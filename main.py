import time

def to_do_logic(
    param_json: dict = None,
    ex_model_param: dict = None,
    in_dir: str = None,
    out_dir: str = None,
    ex_out_dir: str = None,
    is_training: bool = False,
    training_model_path: str = None,
) -> Any:
    print("##################################################")
    print(f"param_json => {param_json}")    
    print(f"ex_model_param => {ex_model_param}")    
    print(f"in_dir => {in_dir}")    
    print(f"out_dir => {out_dir}")    
    print(f"ex_out_dir => {ex_out_dir}")    
    print(f"is_training => {is_training}")    
    print(f"training_model_path => {training_model_path}")    
    print("##################################################")
    
    for i in range(600):
        print(f"Step {i}")
        time.sleep(1)
    accuracy_json = {'a' : 100}
    loss_json = {'b' : 80}
    output_params = {'p1' : 'x', 'p2' : 'y', 'p3' : 10}
    files = []
    return accuracy_json, loss_json, output_params, files

if __name__ == "__main__":
    print("model starts running")
    for i in range(1000):
        print(f"Step {i}")
        time.sleep(1)