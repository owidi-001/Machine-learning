import tensorflow as tf

x=tf.constant(10.0,name='x',dtype=tf.float32)
y=tf.constant(20.0,name='y',dtype=tf.float32)
z=tf.Variable(tf.add(x, y))

# create a session
init=tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)
    print(session.run(y))