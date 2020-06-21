import tensorflow as tf

# 오퍼레이션 생성? constant가 무엇인지??
tensorA = tf.constant("hello world")

print(tensorA.numpy())
# tensorA의 타입
print(type(tensorA.numpy()))


print(tensorA.numpy().decode('utf-8'))
# tensorA의 decode타입
print(type(tensorA.numpy().decode('utf-8')))

'''
텐서 값을 한글을 사용하는 경우
'''

tensorB = tf.constant("안녕 세상아?")

#tensorB에는 한글이 들어가있음
print(tensorB.numpy())
print(tensorB.numpy().decode('utf-8'))

'''
내가 생각하는 응용방법
더하기
빼기
곱하기
'''

tensorC = tf.constant(4)
tensorD = tf.constant(2)
# tensor 더하기
tensorE = tf.add(tensorC, tensorD)

print(tensorE.numpy())

# tensor 곱하기
tensorE = tf.multiply(tensorC, tensorD)

print(tensorE.numpy())

# tensor 수식 계산
tensorE = tensorC-tensorD

print(tensorE.numpy())

'''
tensorflow에서의 행렬곱 계산
'''

tensorA = tf.constant([[3, 4], [1, 5]])
tensorB = tf.constant([[1, 4], [2, 4]])

tensorE = tf.matmul(tensorA, tensorB)

print(tensorE.numpy())


