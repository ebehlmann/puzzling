import input

def split_node(node):
	node_count = int(node[0])
	metadata_count = int(node[1])
	metadata = []
	while len(metadata) < metadata_count:
		metadata.append(int(node.pop()))
	return node[2:], node_count, metadata

test = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

test_split = test.split(' ')

sub_node, node_count, metadata = split_node(test_split)

print(sub_node)
print(node_count)
print(metadata)

