# version 1的数据需要先转换GBK编码，然后再转换回UTF-8编码才能使用，不然会报编码错误，搞不懂

from __future__ import print_function
import glob


def BIO2BMES(input_file, reserve='NAM'):
    print("Convert BIO -> BIOES for file:", input_file)
    with open(input_file, 'r', encoding='utf-8') as in_file:
        fins = in_file.readlines()
    fout = open('./result/'+'aweibo2'+reserve+'.'+input_file.split('.')[-1]+'.bmes','w', encoding='utf-8')
    words, posi_in_words, labels = [], [], []

    for line in fins:
        if len(line) < 3:           # 读到句尾
            sent_len = len(words)
            for idx in range(sent_len):
                if "-" not in labels[idx]:                          # 标签O
                    fout.write(words[idx]+posi_in_words[idx]+" "+labels[idx]+"\n")
                else:
                    label_type = labels[idx].split('-')[-1]
                    if reserve not in label_type:
                        fout.write(words[idx]+posi_in_words[idx]+" O"+"\n")
                    else:
                        if "B-" in labels[idx] or ("I-" in labels[idx] and ((idx != 0 and "-" not in labels[idx-1]) or idx == 0)):   # 源文件存在脏数据，比如训练集的22001行
                            if (idx != sent_len - 1) and ("I-" in labels[idx+1]):
                                fout.write(words[idx]+posi_in_words[idx]+" B-"+label_type+"\n")
                            else:
                                fout.write(words[idx]+posi_in_words[idx]+" S-"+label_type+"\n")
                        elif "I-" in labels[idx]:
                            if (idx != sent_len - 1) and ("I-" in labels[idx+1]):
                                fout.write(words[idx]+posi_in_words[idx]+" M-"+label_type+"\n")
                            else:
                                fout.write(words[idx]+posi_in_words[idx]+" E-"+label_type+"\n")
            fout.write('\n')
            words, posi_in_words, labels = [], [], []
        else:
            pair = line.strip('\n').split()
            words.append(pair[0][0])
            posi_in_words.append(' seg:'+pair[0][1])
            labels.append(pair[-1].upper())
    fout.close()
    print("BMES file generated:")


def main():
    weibo2_bio_files = glob.glob('./weiboNER_2nd_conll.*')
    reserves = ['NOM', 'NAM']
    for file in weibo2_bio_files:
        for reserve in reserves:
            BIO2BMES(file, reserve=reserve)



if __name__ == "__main__":
    main()
