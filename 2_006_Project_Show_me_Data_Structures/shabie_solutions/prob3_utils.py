from collections import Counter

class Node(object):

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f"Node of character: {self.char} | frequency: {self.freq}"

    @staticmethod
    def fusion_nodes(node_1, node_2):
        """
        Combines 2 nodes together, by using them as the leafs of a new node
        
        Parameters
        ----------
        node_1: Node 
            one of the nodes to fuse
        
        node_2: Node
            the other node to fuse
        
        
        Returns
        -------
        Node
            nodes fused, being the leaves of a third parent node
        """
        fused_node = Node()

        if node_1.freq <= node_2.freq:
            fused_node.left = node_1
            fused_node.right = node_2
        else:
            fused_node.left = node_2
            fused_node.right = node_1

        fused_node.freq = node_1.freq + node_2.freq

        return fused_node

class Queue(object):

    def __init__(self, string: str):
        self.arr = [Node(char=c, freq=freq) for c, freq in Counter(string).items()]
        self.sort()

    def sort(self) -> None:
        """
        Sorts the queue by frequency in descending order
        """
        self.arr = sorted(self.arr, key=lambda x: x.freq, reverse=True)

    def fuse_step(self) -> None:
        """
        Applies fusion of two nodes present on the queue; see Node.fusion_nodes()
        """
        low_node_1 = self.arr.pop()
        low_node_2 = self.arr.pop()

        self.arr.append(Node.fusion_nodes(node_1=low_node_1, node_2=low_node_2))
        self.sort()
        

class Tree(object):

    def __init__(self, queue: Queue):

        while len(queue.arr) > 1:  # clever: converts an array of individual nodes to a binary tree
            queue.fuse_step()
        self.root = queue.arr[0]

    def binaryze(self) -> None:
        """
        Binarizes a Tree, by changing Node.char information for a 1/0 value;  recursive launcher
        """

        self.root = self._add_binary_code(self.root)
        self.root.freq = 0

    @staticmethod
    def _add_binary_code(node: Node) -> Node:
        """
        Binarizes a Tree, by changing Node.char information for a 1/0 value
        
        Parameters
        ----------
        node: Node 
            node to modify
        

        Returns
        -------
        Node
            binarized node
        """
        
        if (node.left is None) and (node.right is None):
            return node

        if node.left is not None:
            node.left.freq = 1
            node.left = Tree._add_binary_code(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree._add_binary_code(node.right)

        return node

class HuffmanEncoder(object):
    
    def __init__(self, tree: Tree):
        self.table = self._create_encoding_table(base_code='', node=tree.root)
        self.encode_dict = None
        self.decode_dict = None

        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self) -> None:
        """
        Encoder dictionary constructor
        """
        
        encoder_dict = {}

        for i, element in enumerate(self.table):
            encoder_dict[element[0]] = element[1]

        self.encode_dict = encoder_dict

    def _create_decoder(self) -> None:
        """
        Decoder dictionary constructor
        """
        
        decoder_dict = {}

        for i, element in enumerate(self.table):
            decoder_dict[element[1]] = element[0]

        self.decode_dict = decoder_dict

    def encode(self, text: str) -> str:
        """
        Text encoding method, specific for each encoder
        :param text: text to encode, same as used to construct Huffman Encoder
        :return: text encoded with Huffman algorithm
        """
        coded_text = ''
        for char in text:
            coded_text += self.encode_dict[char]

        return coded_text

    def decode(self, encoded_text: str) -> str:
        """
        Text decoding method, specific for each encoder
        :param encoded_text: text to decoded, same as used to construct Huffman Encoder
        :return: text decoded with Huffman algorithm
        """
        decoded_text = ''

        while len(encoded_text) > 0:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decode_dict.keys():
                    decoded_text += self.decode_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1

        return decoded_text

    @staticmethod
    def _create_encoding_table(base_code: str, node: Node) -> list:
        """
        Creates the basic encoding table by traversing the binary-tree
        :param base_code: base code from previous level of the binary tree
        :param node: node of the tree to search characters on
        :return: list of the characters and their corresponding binary encoding
        """
        if (node.left is None) and (node.right is None):
            return [(node.char, base_code + str(node.freq))]

        if node.freq == -1:
            current_code = ''
        else:
            current_code = base_code + str(node.freq)

        coding_dict = []

        if node.char is not None:
            coding_dict.append((node.char, current_code + str(node.freq)))

        if node.left is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.left))

        if node.right is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.right))

        return coding_dict
