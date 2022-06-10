import psutil

print('RAM used:', psutil.virtual_memory()[2],"GB")
print('RAM used:', psutil.virtual_memory()[3]/1024/1024/1024,"GB")
print('Total RAM:', psutil.virtual_memory()[0]/1024/1024/1024,"GB")
print('RAM usage', psutil.virtual_memory()[2], "%")

if(psutil.virtual_memory()[2] > 20):
    print("Attention! RAM usage is too high!")