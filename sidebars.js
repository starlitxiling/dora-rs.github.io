/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  // tutorialSidebar: [{ type: "autogenerated", dirName: "." }],

  // But you can create a sidebar manually
  guides: [
    {
      type: "category",
      label: "Guides",
      link: { type: "doc", id: "guides/readme" },
      items: [
        {
          type: "autogenerated",
          dirName: "guides",
        },
      ],
    },
  ],
  references: [
    {
      type: "category",
      label: "References",
      link: { type: "doc", id: "references/readme" },
      items: [
        {
          type: "autogenerated",
          dirName: "references",
        },
      ],
    },
  ],
  examples: [
    {
      type: "category",
      label: "Examples",
      link: { type: "doc", id: "examples/readme" },
      items: [
        {
          type: "autogenerated",
          dirName: "examples",
        },
      ],
    },
  ],
  nodes: [
    {
      type: "category",
      label: "Nodes",
      link: { type: "doc", id: "nodes/readme" },
      items: [
        {
          type: "autogenerated",
          dirName: "nodes",
        },
      ],
    },
  ],
};

module.exports = sidebars;
