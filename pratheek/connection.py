
import argparse


import encode_text as en
import generate_images as gen

from os.path import join

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--z_dim', type=int, default=100,
						help='Noise dimension')

	parser.add_argument('--t_dim', type=int, default=256,
						help='Text feature dimension')

	parser.add_argument('--batch_size', type=int, default=64,
						help='Batch Size')

	parser.add_argument('--image_size', type=int, default=128,
						help='Image Size a, a x a')

	parser.add_argument('--gf_dim', type=int, default=64,
						help='Number of conv in the first layer gen.')

	parser.add_argument('--df_dim', type=int, default=64,
						help='Number of conv in the first layer discr.')

	parser.add_argument('--caption_vector_length', type=int, default=4800,
						help='Caption Vector Length')

	parser.add_argument('--n_classes', type=int, default=102,
						help='Number of classes/class labels')

	parser.add_argument('--data_dir', type=str, default="Data",
						help='Data Directory')

	parser.add_argument('--learning_rate', type=float, default=0.0002,
						help='Learning Rate')

	parser.add_argument('--beta1', type=float, default=0.5,
						help='Momentum for Adam Update')

	parser.add_argument('--images_per_caption', type=int, default=30,
						help='The number of images that you want to generate '
	                         'per text description')

	parser.add_argument('--data_set', type=str, default="flowers",
						help='Dat set: MS-COCO, flowers')

	parser.add_argument('--checkpoints_dir', type=str, default="/tmp",
						help='Path to the checkpoints directory')

	parser.add_argument('--text', type=str, default="a_flower_with_red_petals_which_are_pointed",
						help='text to be generated')


	args = parser.parse_args()

	datasets_root_dir = join(args.data_dir, 'datasets')

	# loaded_data = load_training_data(datasets_root_dir, args.data_set,
	# 								 args.caption_vector_length,
	# 								 args.n_classes)
	
    # model_options = {
	# 	'z_dim': args.z_dim,
	# 	't_dim': args.t_dim,
	# 	'batch_size': args.batch_size,
	# 	'image_size': args.image_size,
	# 	'gf_dim': args.gf_dim,
	# 	'df_dim': args.df_dim,
	# 	'caption_vector_length': args.caption_vector_length,
	# 	'n_classes': loaded_data['n_classes'],
	# 	'text':args.text
	# }

	en.encode_main(args.text)

	gen.gen_main(args.data_set, args.t_dim, args.z_dim, args.gf_dim, args.df_dim, args.image_size, args.learning_rate,  args.beta1, args.n_classes, args.caption_vector_length, args.batch_size , args.checkpoints_dir, args.images_per_caption, args.data_dir, args.text, datasets_root_dir)

if __name__ == '__main__':
	main()