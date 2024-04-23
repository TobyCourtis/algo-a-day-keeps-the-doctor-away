function getAdjacentIndices(index: number, numRows: number, numCols: number): number[] {
    const adjacentIndices: number[] = [];

    const row = Math.floor(index / numCols);
    const col = index % numCols;

    for (let dr = -1; dr <= 1; dr++) {
        for (let dc = -1; dc <= 1; dc++) {
            const newRow = row + dr;
            const newCol = col + dc;
            const newIndex = newRow * numCols + newCol;

            if (newRow >= 0 && newRow < numRows && newCol >= 0 && newCol < numCols && newIndex !== index) {
                adjacentIndices.push(newIndex);
            }
        }
    }

    return adjacentIndices;
}