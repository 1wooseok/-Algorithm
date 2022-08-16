function range(start: number, end?:number, step?:number): number[] {
  if (start === undefined) {
    throw new Error("Function range must get 2 parameters (start: number, end: number)");
  }

  let result: number[] = [];

  // All Parameters
  if (start !== undefined && end !== undefined && step !== undefined) {
    if (step < 0) {
      for (let i = start; i >= end; i += step) {
        result.push(i);
      }
    }
    if (step > 0) {
      for (let i = start; i <= end; i += step) {
        result.push(i);
      }
    }
    if (step === 0) {
      result.push(start);
    }
  }

  // Two Parameters
  if (start !== undefined && end !== undefined && step === undefined) {
    if (end < start) {
      for (let i = start; i >= end; i--) {
        result.push(i);
      }
    }
    else {
      for (let i = start; i <= end; i++) {
        result.push(i);
      }
    } 
  }

  // Single Parameters
  if (start !== undefined && end === undefined && step === undefined) {
    if (start === 0) {
      result.push(0);
    }
    else if (start < 0) {
      for (let i = start; i < 0; i++) {
        result.push(i)
      }
    }
    else {
      for (let i = 1; i <= start; i++) {
        result.push(i);
      }
    }
  }
  return result
}

function debugConsole(result: number[], x:number, y?:number, z?:number) {
  console.log(`range(${x}, ${y}, ${z}) should be ${result}`); 
  console.log(`range(${x}, ${y}, ${z}) is ${range(x, y, z)}`);
  
  console.log(" ");
  console.log(" ");
}

console.log(`range(1, 10, 1) should be 1,2,3,4,5,6,7,8,9,10`); 
console.log(`range(1, 10, 1) result is ${range(1, 10, 1)}`);

console.log(" ");
console.log(" ");

console.log(`range(1, 10, 2) should be [1,3,5,7,9]`); 
console.log(`range(1, 10, 2) result is ${range(1, 10, 2)}`);

console.log(" ");
console.log(" ");

console.log(`range(1, 10) should be [1,2,3,4,5,6,7,8,9,10]`); 
console.log(`range(1, 10) is ${range(1, 10, 1)}`);

console.log(" ");
console.log(" ");

console.log(`range(10, 1) should be [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`); 
console.log(`range(10, 1) is ${range(10, 1)}`);

console.log(" ");
console.log(" ");

console.log(`range(10, 1, -2) should be [10, 8, 6, 4, 2]`); 
console.log(`range(10, 1, -2) is ${range(10, 1, -2)}`);

console.log(" ");
console.log(" ");

console.log(`range(5) should be [1, 2, 3, 4, 5]`); 
console.log(`range(5) is ${range(5)}`);

console.log(" ");
console.log(" ");

console.log(`range(-5) should be [-5, -4, -3, -2, -1]`); 
console.log(`range(-5) is ${range(-5)}`);

console.log(" ");
console.log(" ");

debugConsole([5], 5, 5);
debugConsole([5], 5, 5, 0);
debugConsole([5], 5, 5, -1);
debugConsole([], 5, 1, 1);
debugConsole([], 1, 5, -1);
debugConsole([], 1, 5, 6);
debugConsole([0], 0); // f
debugConsole([2], 2, 1, -5);
debugConsole([0, 1, 2, 3, 4, 5], 0, 5); // f
debugConsole([0, -1], 0, -1); // f
debugConsole([0, -1, -2, -3], 0, -3); //
debugConsole([-3, -2, -1, 0], -3, 0); //
debugConsole([0], 0, 0); //
debugConsole([0], 0, 0, 5); //
debugConsole([0], 0, -1, -5); //


