rects_root = 'dataset/ReCTS/'

# dataset with type='TextDetDataset'
rects_train = dict(
    type='TextDetDataset',
    img_prefix=f'{rects_root}img',
    ann_file=f'{rects_root}/line_json_parse/train/labels.txt',
    loader=dict(
        type='HardDiskLoader',
        repeat=4,
        parser=dict(
            type='LineJsonParser',
            keys=['file_name', 'height', 'width', 'annotations'])),
    pipeline=None,
    test_mode=False)

rects_test = dict(
    type='TextDetDataset',
    img_prefix=f'{rects_root}img',
    ann_file=f'{rects_root}/line_json_parse/val/labels.txt',
    loader=dict(
        type='HardDiskLoader',
        repeat=1,
        parser=dict(
            type='LineJsonParser',
            keys=['file_name', 'height', 'width', 'annotations'])),
    pipeline=None,
    test_mode=True)

train_list = [rects_train]
test_list = [rects_test]