function generateCrossword(words) {
    // First, we'll create a grid of empty spaces to hold the puzzle
    const grid = [];
    for (let i = 0; i < 10; i++) {
      grid[i] = [];
      for (let j = 0; j < 10; j++) {
        grid[i][j] = ' ';
      }
    }
  
    // Next, we'll iterate through the list of words and try to place them in the grid
    for (const word of words) {
      let placed = false;
      while (!placed) {
        // Choose a random starting position and direction (horizontal or vertical) for the word
        const startRow = Math.floor(Math.random() * 10);
        const startCol = Math.floor(Math.random() * 10);
        const direction = Math.random() < 0.5 ? 'horizontal' : 'vertical';
  
        // Check if the word fits in the grid starting at the chosen position and direction
        if (canFitWord(grid, word, startRow, startCol, direction)) {
          // If it fits, place the word in the grid
          placeWord(grid, word, startRow, startCol, direction);
          placed = true;
        }
      }
    }
  
    // Finally, we'll return the completed puzzle grid
    return grid;
  }
  
  // This helper function checks if a word can fit in the grid starting at a given position and direction
  function canFitWord(grid, word, row, col, direction) {
    // Check if the word would run off the edge of the grid
    if (direction === 'horizontal' && col + word.length > grid[0].length) {
      return false;
    }
    if (direction === 'vertical' && row + word.length > grid.length) {
      return false;
    }
  
    // Check if any of the spaces the word would occupy are already filled
    for (let i = 0; i < word.length; i++) {
      const r = direction === 'horizontal' ? row : row + i;
      const c = direction === 'horizontal' ? col + i : col;
      if (grid[r][c] !== ' ' && grid[r][c] !== word[i]) {
        return false;
      }
    }
  
    return true;
  }
  
  // This helper function places a word in the grid at a given position and direction
  function placeWord(grid, word, row, col, direction) {
    for (let i = 0; i < word.length; i++) {
      const r = direction === 'horizontal' ? row : row + i;
      const c = direction === 'horizontal' ? col + i : col;
      grid[r][c] = word[i];
    }
  }
  
 