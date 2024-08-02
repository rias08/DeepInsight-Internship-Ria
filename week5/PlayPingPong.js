// Use the mouse to move the paddle from left to right. Keep the ball in the air. If it touches the ground, you lose.

/* VARIABLES */
let paddle, ball, secondBall;
let score = 0;
let round = 1;
let gameOver = false;

/* PRELOAD LOADS FILES */
function preload() {}

function clearScreen() {
  background(224, 224, 224);
}

/* SETUP RUNS ONCE */
function setup() {
  createCanvas(400, 400);
  clearScreen();

  // Create paddle 
  paddle = new Sprite(200, 380, 100, 20);
  paddle.color = color(95, 158, 160);
  paddle.rotationLock = true;

  // Create ball
  ball = new Sprite(100, 50, 20);
  ball.color = color(0, 128, 128);
  ball.direction = 'down';
  ball.speed = 5;
  ball.bounciness = 1;
  ball.friction = 0;

  // Create walls
  walls = new Group();
  walls.w = 10;
  walls.h = 400;
  walls.collider = "static";
  walls.visible = false;

  // Left and right walls
  new walls.Sprite(0, height / 2);
  new walls.Sprite(width, height / 2);

  // Top wall
  let wallTop = new walls.Sprite(width / 2, 0);
  wallTop.rotation = 90;
}

function resetGame() {
  score = 0;
  ball.remove();
  if (secondBall) secondBall.remove();
  ball = new Sprite(120, 50, 20);
  ball.color = color(0, 128, 128);
  ball.direction = 'down';
  ball.speed = 3;
  ball.bounciness = 1;
  ball.friction = 0;
  gameOver = false;
  clearScreen();
}

function nextRound() {
  round++;
  secondBall = new Sprite(100, 50, 20);
  secondBall.color = color(255, 0, 0);
  secondBall.direction = 'down';
  secondBall.speed = 5;
  secondBall.bounciness = 1;
  secondBall.friction = 0;
}

function draw() {
  background(224, 224, 224);

  // Move the paddle
  paddle.moveTowards(mouse.x, 380, 1);

  // When ball collides with paddle bounce off and increase score
  if (ball.collides(paddle)) {
    ball.speed = 8;
    score = score + 1;
    ball.direction = ball.direction + random(-10, 10);
  }
  if (secondBall && secondBall.collides(paddle)) {
    secondBall.speed = 8;
    score = score + 1;
    secondBall.direction = secondBall.direction + random(-10, 10);
  }

  // When ball hits ground you lose
  if (ball.y > 390) {
    ball.y = 430;
    ball.speed = 0;
  }
  if (secondBall && secondBall.y > 390) {
    secondBall.y = 430;
    secondBall.speed = 0;
  }

  // Check if both balls have fallen in round two
  if ((round < 2 && ball.y > 390) || (round === 2 && ball.y > 390 && (!secondBall || secondBall.y > 390))) {
    if (round === 2 && ball.y > 390 && (!secondBall || secondBall.y > 390)) {
      gameOver = true;
    }

    if (gameOver) {
      fill(0);
      textSize(20);
      textAlign(CENTER);
      text("Thank you for playing!", width / 2, height / 2);
    } else {
      fill(0);
      textSize(20);
      textAlign(CENTER);
      text("Your score is: " + score, width / 2, 160); 
      text("Would you like to play again?", width / 2, height / 2);
      text("Press 'r' to play again", width / 2, height / 2 + 20);
      text("or 'n' to move to the next round.", width / 2, height / 2 + 40);

      if (kb.presses('r')) {
        round = 1;
        resetGame();
      } else if (kb.presses('n') && round < 2) {
        resetGame();
        nextRound();
      }
    }
  }

  // Draw the score
  fill(0, 128, 128);
  textAlign(LEFT);
  textSize(20);
  text('Score = ' + score, 10, 30);
}
