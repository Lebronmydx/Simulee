# **Total Detected Real Bug with Positive Feedback**:
```
cudpp: 3 Bugs
CudaSift: 4 Bugs
gunrock: 1 Bug
kaldi: 2 Bugs
Total： 10 Bugs
```

| Project       | Bugs with Positive Feedback | reference                                       |
| ------------- | --------------------------- | ----------------------------------------------- |
| cudpp         | 3                           |https://github.com/cudpp/cudpp/issues/180        |
| CudaSift      | 4                           |https://github.com/Celebrandil/CudaSift/issues/38|
| gunrock       | 2                           |https://github.com/gunrock/gunrock/issues/452    |
| kaldi         | 1                           |https://github.com/kaldi-asr/kaldi/issues/3029   |
| kaldi         | 1                           |https://github.com/kaldi-asr/kaldi/issues/3036   | 

# Performance in different setting
Please see "performance.log" file. 
The kernel function is related to table 4 in performance.log.

# Introduction
In EvolutionaryDetect.py, all functions start with "test_" are detecting synchronization bugs and related to a specify kernel function. You will need Python 2.7 to run them. No other dependency is needed.

### Detailed instruction
arrayfire:
```
test_arrayfire_scan_nofinal_kernel()
test_arrayfire_scan_dim_nofinal_kernel()
test_arrayfire_hamming_matcher_2()
test_arrayfire_hamming_matcher_unroll_1()
test_arrayfire_JacobiSVD()
test_arrayfire_reduce()
test_arrayfire_reduce1()
test_arrayfire_scan_dim()
test_arrayfire_hamming_matcher_1()
test_arrayfire_select_matches()
test_arrayfire_hamming_matcher_unroll_2()
test_arrayfire_descriptor()
test_arrayfire_compute_median()
test_arrayfire_harris_response()
```
kaldi:
```
test_sum_reduced()
test_copy_low_upp()
test_copy_upp_low()
test_add_diag_vec_mat()
test_copy_from_tp()
test_copy_from_mat()
test_slice()
test_kaldi_add_diag()
```

thundersvm:
```
test_thundersvm_nu_smo_solve_kernel()
test_thundersvm_c_smo_solve_kernel()
```

gunrock:
```
test_gunrock_join()
```

CUDA-CNN
```
test_sync_cuda_cnn_g_getCost_3()
```

CudaSift:
```
test_sync_FindMaxCorr()
```

cudpp
```
test_sync_cudpp_sparseMatrixVectorSetFlags()
```


Positive feedback from authors:
```
https://github.com/cudpp/cudpp/issues/180
https://github.com/Celebrandil/CudaSift/issues/38
https://github.com/gunrock/gunrock/issues/452
https://github.com/kaldi-asr/kaldi/issues/3029
https://github.com/kaldi-asr/kaldi/issues/3036
```

# Raw bug log
Raw bug log located in
```
./raw_data_report_script
```

# Bug log parser
log-paser.py is used to parsed raw bug log to get a report.
```
./raw_data_report_script/log-parser.py
```


