import { Sandbox } from "@e2b/code-interpreter";
import "dotenv/config";

// Create a new sandbox
const sbx = await Sandbox.create({ apiKey: process.env.E2B_API_KEY });

// Install the axios package
await sbx.commands.run("npm install axios");

// Run the code
const execution = await sbx.runCode(`
  import axios from "axios";

  const url: string = "https://api.github.com/status";
  const response = await axios.get(url);
  response.data;
`,
  { language: "ts" }
);

console.log(execution);

// Execution {
//   results: [],
//   logs: {
//     stdout: [ "{ message: 'GitHub lives! (2025-05-28 10:49:55 -0700) (1)' }\n" ],
//     stderr: [],
//   },
//   error: undefined,
//   executionCount: 1,
//   text: [Getter],
//   toJSON: [Function: toJSON],
// }
