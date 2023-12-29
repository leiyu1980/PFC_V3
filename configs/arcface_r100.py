from easydict import EasyDict

config = EasyDict()

config.prefix = "arcface-r100-ms1mv2"
config.head = "arcface"
config.input_size = [112, 112]
config.embedding_size = 512
config.depth = "100"
config.batch_size = 256
config.weight_decay = 5e-4
config.lr = 0.1
config.momentum = 0.9
config.epochs = 20
config.margin = 0.5
config.fp16 = True
config.sample_rate = 1.0
config.train_source = "./datasets/ms1mv2.lmdb"
config.val_list = ["lfw", "cfp_fp", "agedb_30"]
config.mask = None
