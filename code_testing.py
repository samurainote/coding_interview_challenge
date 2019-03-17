import numpy as np

m = 10
n = 20
input_matrix = np.random.randint(8, size=(m, n))
tensor2D = input_matrix


m, n = tensor2D.shape[0], tensor2D.shape[1]
# matrix = ex
matrix = np.array(tensor2D, dtype='int32')
# vector = np.reshape(matirx, (1, m * n))
vector = matrix.flatten()
z = matrix.max()
if z < 2:
    print("Not enough depth")
print(vector)
print("------------------------")
mn = m * n
vectores = np.zeros((z, mn), dtype=int)
print(vectores)
print("------------------------")

# one-hot matrix
for i in range(m * n):
    value = vector[i]
    if value != np.nan:
        for zi in range(value):
            vectores[zi, i] = 1
# print(vectores)
print(vectores.shape)
print("------------------------")

# we need at least 8 block in any matrix
counter = 0
for x in range(vectores.shape[0]):
    counter += 1
    if vectores[x].sum() < 8:
        z = counter
        print(z)

onehot = vectores[:z]
print(onehot)
print(onehot.shape)

# ３D arrayにする
onehot3D = np.reshape(onehot, (onehot.shape[0], m, n))
print(onehot3D[0])
print("------------------------")
print(onehot3D.shape)
print("------------------------")

onehot2D = onehot3D[0]
onehot1D = onehot2D[1]
print(onehot1D)

onehot2D[2,3]


# 計算する 基本0が1に囲まれてたらOK
total_num = 0
for zi in range(1, onehot3D.shape[0]):

    onehot2D = onehot3D[zi]
    # マトリクス単位
    # block_num = 0
    matrix_block = 0
    for yi in range(1, onehot2D.shape[0]-1):
        onehot1D = onehot2D[yi]
        # ブロックごと
        block_num = 0
        for xi in range(1, len(onehot1D)-1):
            counter = 0

            target = onehot2D[yi, xi]
            # we only concern about hole(=0) to put water
            if target != np.nan:
                continue
            counter += 1
            # onehot2D[yi+1, xi] != np.nan and onehot2D[yi, xi+1] != np.nan:
            # x方向について
            axis1 = onehot2D[yi]
            checker = 0
            for a1 in range(xi):
                checker += axis1[a1]
            if checker == np.nan:
                continue
            checker = 0
            for a1 in range(xi, len(axis1)):
                checker += axis1[a1]
            if checker == np.nan:
                continue

            # y方向について
            for i in range(onehot2D.shape[0]):
                checker = 0
                for a0 in range(yi):
                    checker += axis1[a0][xi]
                if checker == np.nan:
                    continue
                checker = 0
                for a0 in range(yi, len(axis0)):
                    checker += axis1[a0][xi]
                if checker == np.nan:
                    continue

            if zi == 1:
                if onehot3D[0, yi, xi] == 0:
                    continue

            block_num += 1
        matrix_block = block_num
        # if block_num != counter:
            # continue
    total_num += matrix_block

print("Ammount of water is: ", total_num)
