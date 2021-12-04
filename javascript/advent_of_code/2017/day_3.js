function build_spiral(final_square) {
	let direction = 'E';
	let spiral = [[1]];
	let current_array = 0;
	for (var i = 2; i <= final_square; i++) {
		if (direction == 'E'){
			// add to the end of the current array and, if we're past the end, turn N
			spiral[current_array].push(i);
			if(spiral.length == 1 || spiral[current_array].length > spiral[current_array-1].length) {
				direction = 'N';
			}
		} else if (direction == 'N') {
			// if there's an array to the north, go to that. Otherwise prepend one
			if(current_array == 0) {
				spiral.unshift([i]);
				direction = 'W';
			} else {
				current_array -= 1;
				spiral[current_array].push(i);
			}
		} else if (direction == 'W') {
			// add to the beginning of the current array and, if we're past the end, turn S
			spiral[current_array].unshift(i);
			if(spiral.length == 1 || spiral[current_array].length > spiral[current_array+1].length) {
				direction = 'S';
			}
		} else {
			if(current_array == spiral.length - 1) {
				spiral.push([i]);
				current_array += 1;
				direction = 'E';
			} else {
				current_array += 1;
				spiral[current_array].unshift(i);
			}
		}

	}
	return spiral;
}

document.querySelector('#part1Button').addEventListener('click', () => {
	input = document.querySelector('#puzzleInput').value;
	part1Result = input;
	var part1Display = document.querySelector('#part1Result');
	part1Display.textContent = part1Result;
});

document.querySelector('#part2Button').addEventListener('click', () => {
	input = document.querySelector('#puzzleInput').value;
	part2Result = input;
	var part2Display = document.querySelector('#part2Result');
	part2Display.textContent = part2Result;
});