export default function appendToEachArrayValue(array, appendString) {
  const Arr = [];
  for (const idx of array) {
    Arr.push(appendString + idx);
  }

  return Arr;
}
