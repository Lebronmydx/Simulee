from DataStructure import *
from MainProcess import construct_memory_execute_mode
from MainProcess import parse_target_memory_and_checking_sync


# nv-svc fix bugs
# plus: 168 - 175 has sync bugs. return index[0] while index[0] = -f
if __name__ == '__main__':
    test_block = Block((-1, -1, 0), (1, 1, 1))
    test_thread = Thread((-1, -1, 0), (34, 1, 1))
    num_elements = DataType('i32')
    num_elements.set_value(2)
    row_len = DataType('i32')
    row_len.set_value(2)
    float_elements = DataType('float')
    float_elements.set_value(3.0)
    eps_float = DataType('float')
    eps_float.set_value(2.0)
    global_env_test = Environment()
    shared_memory_test = DataType("[256 x i32]*")
    shared_memory_test.set_value("@_ZZ19nu_smo_solve_kernelPKiPfS1_S1_S0_ifPKfS3_ifS1_E10shared_mem")
    global_env_test.add_value("@_ZZ19nu_smo_solve_kernelPKiPfS1_S1_S0_ifPKfS3_ifS1_E10shared_mem", shared_memory_test)
    memory_container = MemoryContainer()
    memory_container.add_new_memory("@_ZZ19nu_smo_solve_kernelPKiPfS1_S1_S0_ifPKfS3_ifS1_E10shared_mem")
    global_env_test.add_value("memory_container", memory_container)
    # i32* %label, float* %f_values, float* %alpha, float* %alpha_diff, i32* %working_set, i32 %ws_size, float %C,
    # float* %k_mat_rows, float* %k_mat_diag, i32 %row_len, float %eps, float* %diff_and_bias
    args = {
        "%label": DataType("i32*"),
        "%f_values": DataType("float*"),
        "%alpha": DataType("float*"),
        "%alpha_diff": DataType("float*"),
        "%working_set": DataType("i32*"),
        "%ws_size": num_elements,
        "%C": float_elements,
        "%k_mat_rows": DataType("float*"),
        "%k_mat_diag": DataType("float*"),
        "%row_len": row_len,
        "%eps": eps_float,
        "%diff_and_bias": DataType("float*"),
        "main_memory": {
            'global': None,
            'shared': "@_ZZ19nu_smo_solve_kernelPKiPfS1_S1_S0_ifPKfS3_ifS1_E10shared_mem",
        }
    }
    args["%label"].set_value("%label")
    args["%f_values"].set_value("%f_values")
    args["%alpha"].set_value("%alpha")
    args["%alpha_diff"].set_value("%alpha_diff")
    args["%working_set"].set_value("%working_set")
    args["%k_mat_rows"].set_value("%k_mat_rows")
    args["%k_mat_diag"].set_value("%k_mat_diag")
    args["%diff_and_bias"].set_value("%diff_and_bias")
    Function.read_function_from_file("./thundersvm/thundersvm.ll", global_env_test)
    raw_code = global_env_test.get_value("@_Z19nu_smo_solve_kernelPKiPfS1_S1_S0_ifPKfS3_ifS1_")
    construct_memory_execute_mode(test_block, test_thread, 100, 256, raw_code.raw_codes, args,
                                  parse_target_memory_and_checking_sync, parse_target_memory_and_checking_sync,
                                  global_env_test, False)
