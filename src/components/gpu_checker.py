import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        # Get details of each GPU
        details = tf.config.experimental.get_device_details(gpu)
        print(f"GPU Name: {details['device_name']}")
else:
    print("No GPUs found.")