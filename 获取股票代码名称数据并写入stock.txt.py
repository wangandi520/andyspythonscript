import adata
from pypinyin import pinyin, lazy_pinyin, Style

# pip install adata pypinyin opencc-python-reimplemented

writeData = []
res_df = adata.stock.info.all_code()
for tempIndex in range(0, len(res_df['stock_code'])):
    # 格式1分成每行
    # writeData.append(res_df['exchange'][tempIndex].lower() + res_df['stock_code'][tempIndex] + ',' + ''.join(lazy_pinyin(res_df['short_name'][tempIndex], style=Style.FIRST_LETTER)) + ',' + res_df['short_name'][tempIndex] + '\n')
    # 格式2写成一个列表
    writeData.append("'" + res_df['exchange'][tempIndex].lower() + res_df['stock_code'][tempIndex] + ',' + ''.join(lazy_pinyin(res_df['short_name'][tempIndex], style=Style.FIRST_LETTER)) + ',' + res_df['short_name'][tempIndex] + "',")
newFile = open('stock.txt', mode='w', encoding='UTF-8')
newFile.writelines(writeData)
newFile.close()