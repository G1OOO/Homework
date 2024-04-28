var obj1 = {
    privilege: "Admin",
    color: "Blue",
    width: 100,
    height: 200
};

var obj2 = {
    privilege: "User",
    color: "Red",
    width: 150,
    height: 250
};

obj1.privilege = "Super Admin";
obj1.color = "Green";
obj2.width = 200;
obj2.height = 300;

console.log("Modified obj1:", obj1);
console.log("Modified obj2:", obj2);