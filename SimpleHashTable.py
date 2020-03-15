
class HashTable :
    tableSize = 0;
    hTable = None;
    
    # 초기화
    def __init__(self, size) :
        if self.tableSize != 0 :
            print("already exist. initailize : input 0 ");
            return;
        self.tableSize = size;
        self.hTable = list([0 for i in range(self.tableSize)]);
        print("hTable  ",self.hTable);
    
    # 해쉬함수
    def hashFunc(self, key) :
        print("key : ", key);
        return key%5;
    
    # 데이터 세팅
    def setData(self, inputData) :
        targAddr = self.hashFunc(inputData);
        self.hTable[targAddr] = inputData;
    
    # 테이블 전체 출력
    def descHashTable(self) : 
        targTable = self.hTable;
        for i in range(self.tableSize):
            #print("i :", i);
            printData = "";
            if targTable[i] != None :
                printData = targTable[i];
                
            print("addr", i, ":", printData);
    
    # 데이터 출력 및 꺼냄
    def getData(self, addr) :
        hashTableAddrDAta = self.hTable[self.hashFunc(addr)];
        if hashTableAddrDAta == None :
            hashTableAddrDAta = "";
            
        print(hashTableAddrDAta);
        
        return hashTableAddrDAta;
        
# TEST

hashTable = HashTable(10);

hashTable.setData(2);

hashTable.descHashTable();
        
hashTable.getData(2);        

    

