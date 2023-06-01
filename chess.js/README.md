chess.js is a TypeScript chess library used for chess move generation/validation, piece placement/movement, and check/checkmate/stalemate detection - basically everything but the AI.

chess.js has been extensively tested in node.js and most modern browsers.

Installation
Run the following command to install the most recent version of chess.js from NPM:

npm install chess.js
Import into your project
Modern way (ESM)
import { Chess } from 'chess.js'
If you want to use it in a browser you can import as module like this:

<script type="module">
  import { Chess } from 'chess.js'
</script>
Old way (CommonJS)
const { Chess } = require('chess.js')
Example Code
The code below plays a random game of chess:

const chess = new Chess()

while (!chess.isGameOver()) {
  const moves = chess.moves()
  const move = moves[Math.floor(Math.random() * moves.length)]
  chess.move(move)
}
console.log(chess.pgn())
User Interface
By design chess.js is a headless library and does not include user interface elements. Many developers have successfully integrated chess.js with the chessboard.js library. See chessboard.js - Random vs Random for an example.

Move & PGN Parsers
This library includes two parsers (permissive and strict) which are used to parse different forms of chess move notation. The permissive parser (the default) is able to handle many derivates of algebraic notation (e.g. Nf3, g1f3, g1-f3, Ng1f3, Ng1-f3, Ng1xf3). The strict parser only accepts moves in Standard Algebraic Notation and requires that they strictly adhere to the specification. The strict parser runs slightly faster but is much less forgiving of non-standard notation.

API
Constructor: Chess([ fen ])
The Chess() constructor takes an optional parameter which specifies the board configuration in Forsyth-Edwards Notation (FEN). Throws an exception if an invalid FEN string is provided.

// board defaults to the starting position when called with no parameters
const chess = new Chess()

// pass in a FEN string to load a particular position
const chess = new Chess(
  'r1k4r/p2nb1p1/2b4p/1p1n1p2/2PP4/3Q1NB1/1P3PPP/R5K1 b - - 0 19'
)
