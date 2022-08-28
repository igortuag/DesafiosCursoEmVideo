d = int(input("Uma diatancia em metros: "))
print("A medida de {} corresponde a \n{}km \n{}hm \n{}am \n{}dm \n{}cm \n{}mm"
      .format(d, d/1000, d/100, d/10, d*10, d*100, d*1000))