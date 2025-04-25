
import React, { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { toast } from "sonner";
import { Card } from "@/components/ui/card";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

const ColumnConverter = () => {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [prefix, setPrefix] = useState('');
  const [suffix, setSuffix] = useState('');
  const [separator, setSeparator] = useState(', ');

  useEffect(() => {
    if (!input.trim()) {
      setOutput('');
      return;
    }

    const result = input
      .split(/[\n\t]+/)
      .map(item => item.trim())
      .filter(Boolean)
      .map(item => `${prefix}${item}${suffix}`)
      .join(separator);

    setOutput(result);
  }, [input, prefix, suffix, separator]);

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
    setPrefix('');
    setSuffix('');
    setSeparator(', ');
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

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">
                Prefix
              </label>
              <Input
                type="text"
                placeholder="e.g., '"
                value={prefix}
                onChange={(e) => setPrefix(e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">
                Suffix
              </label>
              <Input
                type="text"
                placeholder="e.g., '"
                value={suffix}
                onChange={(e) => setSuffix(e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">
                Separator
              </label>
              <Select
                value={separator}
                onValueChange={setSeparator}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Choose separator" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value=", ">Comma with space (, )</SelectItem>
                  <SelectItem value=",">Comma only (,)</SelectItem>
                  <SelectItem value="; ">Semicolon with space (; )</SelectItem>
                  <SelectItem value=";">Semicolon only (;)</SelectItem>
                  <SelectItem value=" | ">Pipe with spaces ( | )</SelectItem>
                  <SelectItem value="|">Pipe only (|)</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>

          <div className="flex justify-center">
            <Button
              onClick={clearAll}
              variant="outline"
            >
              Clear All
            </Button>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium text-gray-700">
              Output (Comma-Separated List)
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
            Copy Comma-Separated List
          </Button>
        </div>
      </Card>
    </div>
  );
};

export default ColumnConverter;

