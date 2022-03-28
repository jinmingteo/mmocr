_base_ = [
    '../../_base_/runtime_10e.py',
    '../../_base_/schedules/schedule_sgd_1200e.py',
    '../../_base_/det_models/dbnet_r18_fpnc.py',
    '../../_base_/det_datasets/ctw_dataset.py',
    '../../_base_/det_datasets/rects_dataset.py',
    '../../_base_/det_pipelines/dbnet_pipeline.py'
]

train_list = [{{_base_.ctw_train}}, {{_base_.rects_train}}] 
test_list = [{{_base_.ctw_test}}, {{_base_.rects_test}}]

train_pipeline_r18 = {{_base_.train_pipeline_r18}}
test_pipeline_1333_736 = {{_base_.test_pipeline_1333_736}}

data = dict(
    samples_per_gpu=16,
    workers_per_gpu=8,
    val_dataloader=dict(samples_per_gpu=16),
    test_dataloader=dict(samples_per_gpu=16),
    train=dict(
        type='UniformConcatDataset',
        datasets=train_list,
        pipeline=train_pipeline_r18),
    val=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline_1333_736),
    test=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline_1333_736))

evaluation = dict(interval=1, metric='hmean-iou', save_best='0_hmean-iou_hmean', rule='greater')
total_epochs = 3