var input;
var part1Result;
var part2Result;

function getCaptchaNext(input) {
	var sum = 0;

	for(var i = 0; i < input.length; i++) {
		if(i == input.length - 1) {
			if(input[0] == input[i]) {
				sum += Number(input[i]);
			}
		} else {
			if(input[i] == input[i+1]) {
				sum += Number(input[i]);
			}
		}
	}

	return sum;
}

function getCaptchaHalfwayAround(input) {
	var sum = 0;
	halfway_around = input.length / 2;

	for(var i = 0; i < input.length; i++) {
		compare_to = i + halfway_around;
		if(compare_to > input.length) {
			compare_to -= input.length;
		}
		if(input[i] == input[compare_to]) {
			sum += Number(input[i]);
		}
	}

	return sum;
}

document.querySelector('#part1Button').addEventListener('click', () => {
	input = document.querySelector('#puzzleInput').value;
	part1Result = getCaptchaNext(input);
	var part1Display = document.querySelector('#part1Result');
	part1Display.textContent = part1Result;
});

document.querySelector('#part2Button').addEventListener('click', () => {
	input = document.querySelector('#puzzleInput').value;
	part2Result = getCaptchaHalfwayAround(input);
	var part2Display = document.querySelector('#part2Result');
	part2Display.textContent = part2Result;
});