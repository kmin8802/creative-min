class Node:
    def __init__(self, data, next= None, prev=None):
        self.data = data;
        self.next = next;
        self.prev = prev;
# 
class DlListMng:
    cur = None;
    head = None;
    tail = None;
        
    def __init__(self, node):
        self.head = node;
        self.cur = self.head;
        self.tail = self.head;
    # 추가     
    def add(self, data):
        if self.head == None :
            self.head = data;
            self.cur = self.head;
            self.tail = self.head;
        else :
            # 기존의 cur가 cur의 prev가 됨, 기존의 cur가 new의 prev가 됨
            # cur 가 new가 됨, cur의 tail이 new가 됨
            temp = self.cur;
            temp.next = data;
            
            self.cur = data;
            self.cur.prev = temp;
            #self.cur.next = data;
            self.tail = data;
    # 삭제
    def deleteNode(self, target):
        existFlag = False;
        
        if(self.head.data == target.data):
            tempNode = self.head.next;
            del self.head;
            self.head = tempNode;
            existFlag = True;
            
        elif(self.tail.data == target.data):
            tempNode = self.tail.prev;
            del self.tail;
            self.tail = tempNode;
            existFlag = True;
        # cmt 1
        #print("before for : ", self.head);
        
        node = self.head;   
        while node.next :
            # cmt 2
            #print("after for : ", node.data);
            
            if(node.data == target.data):
                # cmt 3
                #print("del  : ", node.data);
                existFlag = True;
                tempNode = node;
                
                # cmt 4
                #print("node.prev.next : ", node.prev.next);
                #print("node.next.prev : ", node.next.prev);
                node.prev.next = node.next;
                node.next.prev = node.prev;
                del tempNode;
            node = node.next;
        
        if(existFlag == False):
            print("Not Exists");
            return;
        
        else :
            print(target.data, "deleted");
            return;
            
    def printData(self):
        if(self.head == None) :
            print("Empty");
            return ;
        
        else :
            
            node = self.head;
            cnt = 0;
            while node:
                cnt = cnt+1;
                print("No.", cnt, " : ", node.data);
                node = node.next
                
    # 탐색 - 2번째 인자 True이면 몇 번째에 있는 지 알려줌. False이면 존재여부만 알려줌
    def searchNode(self, target, isPos):
        
        if(str(type(isPos)) != "<class 'bool'>"):
            print("Invalid Input!!! 3rd arg");
            return;
        else:
            if(isPos == True):
                return self.existsTargetPos(target);
            
            else :
                return self.existsTargetBool(target);
    
    # 현재 노드리스트에 존재하는지 여부를 알려줌
    def existsTargetBool(self, target):
        if(self.head == None):
            print("Empty");
            return False;
        
        else :
            node = self.head;
            while node:
                if(node.data == target):
                    print("Exists True");
                    return True;
                node = node.next;
                
            print("Not Exists");
            return False;
    
    # 현재 노드리스트 몇 번재 있는 지 알려줌
    def existsTargetPos(self, target):
        if(self.head == None):
            print("Empty");
            return False;
        
        else :
            node = self.head;
            cnt = 0;
            existsBool = False;
            
            while node:
                cnt = cnt+1;
                if(node.data == target):
                    print("No.", cnt);
                    existsBool = True;
                    
                node = node.next;
            
            if(existsBool == True):
                return True;
            
            else :
                print("Not Exists");
                return False;
    # cur 데이터        
    def getData(self):
        return self.cur.data;
        
testNode = Node(1);
# 초기화
testList = DlListMng(testNode);

# add
testList.add(Node(10));
testList.add(Node(2));
testList.add(Node(3));
testList.add(Node(7));
testList.add(Node(5));
testList.add(Node(5));
testList.add(Node(5));
testList.add(Node(6));
testList.add(Node(8));

# 출력부분
testList.printData();  

# 삭제
testList.deleteNode(Node(5));
testList.deleteNode(Node(4));

# 출력부분
testList.printData();

# 탐색
testList.searchNode(7, False);
testList.searchNode(7, True);
testList.searchNode(5, False);
testList.searchNode(5, True);
