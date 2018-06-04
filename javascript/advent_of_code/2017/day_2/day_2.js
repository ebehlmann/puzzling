function get_checksum (input) {
	checksum = 0;
	for (var i = 0; i < input.length; i++) {
		row = input[i].split('\t');
		row_ints = []
		for (var j = 0; j < row.length; j++) {
			row_ints.push(Number(row[j]));
		}
		max = Math.max(...row_ints);
		min = Math.min(...row_ints);
		checksum += max-min;
	}
	return checksum;
}

function find_divisors(list_of_numbers) {
	for (var i = 0; i < list_of_numbers.length - 1; i++) {
		for (var j = i + 1; j < list_of_numbers.length; j++) {
			if(list_of_numbers[i] % list_of_numbers[j] == 0) {
				return list_of_numbers[i] / list_of_numbers[j];
			}
			if (list_of_numbers[j] % list_of_numbers[i] == 0) {
				return list_of_numbers[j] / list_of_numbers[i];
			}
		}
	}
	return null;
}

function get_checksum_part_2 (input) {
	checksum = 0;
	for (var i = 0; i < input.length; i++) {
		row = input[i].split('\t');
		row_ints = []
		for (var j = 0; j < row.length; j++) {
			row_ints.push(Number(row[j]));
		}
		checksum += find_divisors(row_ints);
	}
	return checksum;
}

document.querySelector('#part1Button').addEventListener('click', () => {
	input = document.querySelector('#puzzleInput').value;
	splitted = input.split('\n');
	part1Result = get_checksum(splitted);
	var part1Display = document.querySelector('#part1Result');
	part1Display.textContent = part1Result;
});

document.querySelector('#part2Button').addEventListener('click', () => {
	input = document.querySelector('#puzzleInput').value;
	splitted = input.split('\n');
	part2Result = get_checksum_part_2(splitted);
	var part2Display = document.querySelector('#part2Result');
	part2Display.textContent = part2Result;
});
