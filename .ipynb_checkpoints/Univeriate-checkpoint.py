class Univeriate():
    def quanQual(dataset):
        qual = []
        quan = []
        for columnName in dataset.columns:
            # print(columnName)
            if(dataset[columnName].dtype == 'O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return qual,quan

     
    