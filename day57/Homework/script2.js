var object1 = {
    name: "Object 1",
    property1: "Value 1",
    property2: "Value 2"
  };

  var object2 = {
    name: "Object 2",
    property1: "Initial Value",
    property2: "Initial Value"
  };

  console.log("Before modification:");
  console.log("Object 1:", object1);
  console.log("Object 2:", object2);

  object1.property1 = "New Value 1";
  object1.property2 = "New Value 2";

  object2.property1 = "Another New Value 1";
  object2.property2 = "Another New Value 2";

  console.log("After modification:");
  console.log("Object 1:", object1);
  console.log("Object 2:", object2);