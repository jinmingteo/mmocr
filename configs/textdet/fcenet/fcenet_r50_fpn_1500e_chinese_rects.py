_base_ = [
    '../../_base_/runtime_10e.py',
    '../../_base_/schedules/schedule_sgd_1500e.py',
    '../../_base_/det_models/fcenet_r50_fpn.py',
    '../../_base_/det_datasets/rects_dataset.py',
    '../../_base_/det_pipelines/fcenet_pipeline.py'
]

train_list = [{{_base_.rects_train}}] 
test_list = [{{_base_.rects_test}}]

train_pipeline_icdar2015 = {{_base_.train_pipeline_icdar2015}}
test_pipeline_icdar2015 = {{_base_.test_pipeline_icdar2015}}

data = dict(
    samples_per_gpu=8,
    workers_per_gpu=2,
    val_dataloader=dict(samples_per_gpu=1),
    test_dataloader=dict(samples_per_gpu=1),
    train=dict(
        type='UniformConcatDataset',
        datasets=train_list,
        pipeline=train_pipeline_icdar2015),
    val=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline_icdar2015),
    test=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline_icdar2015))

evaluation = dict(interval=10, metric='hmean-iou')
