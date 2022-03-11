ctw_root = 'dataset/ctwdataset/'

# dataset with type='TextDetDataset'
ctw_train = dict(
    type='TextDetDataset',
    img_prefix=f'{ctw_root}images',
    ann_file=f'{ctw_root}annotations/line_json_parse/train/labels.txt',
    loader=dict(
        type='HardDiskLoader',
        repeat=4,
        parser=dict(
            type='LineJsonParser',
            keys=['file_name', 'height', 'width', 'annotations'])),
    pipeline=None,
    test_mode=False)

ctw_test = dict(
    type='TextDetDataset',
    img_prefix=f'{ctw_root}images',
    ann_file=f'{ctw_root}annotations/line_json_parse/val/labels.txt',
    loader=dict(
        type='HardDiskLoader',
        repeat=1,
        parser=dict(
            type='LineJsonParser',
            keys=['file_name', 'height', 'width', 'annotations'])),
    pipeline=None,
    test_mode=True)

train_list = [ctw_train]
test_list = [ctw_test]