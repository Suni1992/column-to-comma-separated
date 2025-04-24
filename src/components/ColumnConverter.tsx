
import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { toast } from "sonner";
import { Card } from "@/components/ui/card";

const ColumnConverter = () => {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');

  const convertToList = () => {
    if (!input.trim()) {
      toast.error("Please enter some text to convert");
      return;
    }

    // Split by newlines and/or tabs, filter empty lines, and join with commas
    const result = input
      .split(/[\n\t]+/)
      .map(item => item.trim())
      .filter(Boolean)
      .join(', ');

    setOutput(result);
    toast.success("Text converted successfully!");
  };

  const copyToClipboard = async () => {
    if (!output) {
      toast.error("Nothing to copy!");
      return;
    }

    try {
      await navigator.clipboard.writeText(output);
      toast.success("Copied to clipboard!");
    } catch (err) {
      toast.error("Failed to copy to clipboard");
    }
  };

  const clearAll = () => {
    setInput('');
    setOutput('');
    toast("All cleared!");
  };

  return (
    <div className="flex flex-col items-center min-h-screen bg-gray-50 p-4">
      <Card className="w-full max-w-3xl space-y-6 p-6 bg-white shadow-lg">
        <h1 className="text-2xl font-bold text-center text-gray-800">
          Column to Comma-Separated List Converter
        </h1>
        
        <div className="space-y-4">
          <div className="space-y-2">
            <label className="text-sm font-medium text-gray-700">
              Input (paste your column data here)
            </label>
            <Textarea
              placeholder="Paste your column data here...&#10;One item per line&#10;or separated by tabs"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              className="min-h-[200px] font-mono"
            />
          </div>

          <div className="flex justify-center space-x-4">
            <Button
              onClick={convertToList}
              className="bg-blue-600 hover:bg-blue-700"
            >
              Convert
            </Button>
            <Button
              onClick={clearAll}
              variant="outline"
            >
              Clear All
            </Button>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium text-gray-700">
              Output (comma-separated list)
            </label>
            <Textarea
              value={output}
              readOnly
              className="min-h-[100px] font-mono bg-gray-50"
            />
          </div>

          <Button
            onClick={copyToClipboard}
            className="w-full"
            disabled={!output}
          >
            Copy to Clipboard
          </Button>
        </div>
      </Card>
    </div>
  );
};

export default ColumnConverter;
