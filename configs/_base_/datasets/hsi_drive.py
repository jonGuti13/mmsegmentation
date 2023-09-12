#img_norm_cfg = dict(
#    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
#crop_size = (512, 1024)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    #dict(type='Resize', img_scale=(2048, 1024), ratio_range=(0.5, 2.0)),
    #dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    #dict(type='RandomFlip', flip_ratio=0.5),
    #dict(type='PhotoMetricDistortion'),
    #dict(type='Normalize', **img_norm_cfg),
    #dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    #dict(type='DefaultFormatBundle'),
    #dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    #dict(
        #type='MultiScaleFlipAug',
        #img_scale=(2048, 1024),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
        #flip=False,
        #transforms=[
        #    dict(type='Resize', keep_ratio=True),
        #    dict(type='RandomFlip'),
        #    dict(type='Normalize', **img_norm_cfg),
        #    dict(type='ImageToTensor', keys=['img']),
        #    dict(type='Collect', keys=['img']),
        #])
]

train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='InfiniteSampler', shuffle=True),
    dataset=dict(
        type='HSIDrive20',
        data_root='data/HSIDrive20',
        data_prefix=dict(
            img_path='images/training', seg_map_path='annotations/training'),
        pipeline=train_pipeline))

val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type='HSIDrive20',
        data_root='data/HSIDrive20',
        data_prefix=dict(
            img_path='images/validation', seg_map_path='annotations/validation'),
        pipeline=test_pipeline))

test_dataloader = val_dataloader
val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
test_evaluator = val_evaluator